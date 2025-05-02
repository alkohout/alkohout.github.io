#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Logging macros */
#ifndef NDEBUG
# define LOG_INFO(fmt, ...)  fprintf(stderr, "[INFO]  " fmt "\n", ##__VA_ARGS__)
#else
# define LOG_INFO(fmt, ...)
#endif
# define LOG_ERROR(fmt, ...) fprintf(stderr, "[ERROR] " fmt "\n", ##__VA_ARGS__)

/*
 * decimate()
 *
 * Apply a 2nd-order Butterworth low-pass filter to `input` of length n_in,
 * then downsample by the integer factor step = sr_in/sr_out and store in `output`
 * (length n_out).
 *
 * Parameters:
 *   input   pointer to the input samples (length n_in)
 *   output  pointer to the output buffer (length n_out)
 *   sr_in   original sample rate
 *   sr_out  desired (lower) sample rate
 *   n_in    number of input samples
 *   n_out   number of output samples
 *
 * Returns:
 *   0 on success, –1 on error (invalid rates or memory allocation failure)
 */
int decimate(const long double *input,
             long double       *output,
             float              sr_in,
             float              sr_out,
             size_t             n_in,
             size_t             n_out)
{
    /* Must downsample by integer factor */
    if (sr_out <= 0 || sr_in <= 0) {
        LOG_ERROR("Sample rates must be positive");
        return -1;
    }
    float ratio = sr_in / sr_out;
    size_t step = (size_t)roundf(ratio);
    if (fabsf(ratio - step) > 1e-6f) {
        LOG_ERROR("Non-integer downsampling ratio: sr_in/sr_out = %f", ratio);
        return -1;
    }

    /* Allocate temporary buffer for filtered data */
    long double *filtered = malloc(n_in * sizeof *filtered);
    if (!filtered) {
        LOG_ERROR("Memory allocation failure");
        return -1;
    }

    /* Select filter coefficients based on known sample rates */
    long double a0, a1, a2, b0, b1, b2;
    if (fabsf(sr_in - 8.0f) < 1e-6f && fabsf(sr_out - 0.5f)  < 1e-6f) {
        /* 8 Hz → 0.5 Hz cutoff */
        a0 = 1.0L;         
        a1 = -1.454243586251585L; 
        a2 =  0.574061915083955L;
        b0 = 0.029954582208092L; 
        b1 = 0.059909164416185L; 
        b2 = 0.029954582208092L;
        LOG_INFO("Using Butterworth: 8 Hz sample, 0.5 Hz cutoff");
    }
    else if (fabsf(sr_in - 64.0f) < 1e-6f && fabsf(sr_out - 2.0f)    < 1e-6f) {
        /* 64 Hz → 2 Hz cutoff */
        a0 = 1.0L;         
        a1 = -1.723776172762509L; 
        a2 =  0.757546944478829L;
        b0 = 0.008442692929080L; 
        b1 = 0.016885385858160L; 
        b2 = 0.008442692929080L;
        LOG_INFO("Using Butterworth: 64 Hz sample, 2 Hz cutoff");
    }
    else {
        LOG_ERROR("Unsupported sample-rate pair: %f → %f", sr_in, sr_out);
        free(filtered);
        return -1;
    }

    /* Zero the output buffer */
    for (size_t i = 0; i < n_out; i++) {
        output[i] = 0.0L;
    }

    /* Apply the filter in direct form II */
    if (n_in >= 1) filtered[0] = input[0];
    if (n_in >= 2) filtered[1] = input[1];
    for (size_t i = 2; i < n_in; i++) {
        filtered[i] = (b0*input[i] +
                       b1*input[i-1] +
                       b2*input[i-2] -
                       a1*filtered[i-1] -
                       a2*filtered[i-2]) / a0;
    }

    /* Downsample by picking every `step`-th sample */
    size_t out_idx = 0;
    for (size_t in_idx = 0; in_idx < n_in; in_idx += step) {
        if (out_idx >= n_out) {
            LOG_ERROR("Output buffer overrun at index %zu", out_idx);
            break;
        }
        output[out_idx++] = filtered[in_idx];
    }

    free(filtered);
    LOG_INFO("Decimation complete: factor = %zu", step);
    return 0;
}
