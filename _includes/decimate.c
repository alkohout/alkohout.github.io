
/******************************************************************************
 * Function: decimate
 * Purpose: Decimates (downsamples) a signal after applying an anti-aliasing
 *          Butterworth filter
 * 
 * Parameters:
 *   in[]  - Input signal array
 *   out[] - Output decimated signal array
 *   sr1   - Input sampling rate (Hz)
 *   sr2   - Output sampling rate (Hz)
 *   n1    - Length of input array
 *   n2    - Length of output array
 * 
 * Returns:
 *   void
 * 
 * Notes:
 *   - Implements 2nd order Butterworth filter
 *   - Supports two specific sampling rate combinations:
 *     1. 8 Hz input (sr1=0.125) with 0.5 Hz cutoff
 *     2. 64 Hz input (sr1=0.015625) with 2 Hz cutoff
 *   - Requires integer ratio between input and output sampling rates
 *   - Includes bounds checking and error logging
 * 
 * Filter Coefficients:
 *   8 Hz sampling:  a = [1.0, -1.4542, 0.5741]
 *                   b = [0.0300, 0.0599, 0.0300]
 *   64 Hz sampling: a = [1.0, -1.7238, 0.7575]
 *                   b = [0.0084, 0.0169, 0.0084]
 * 
 *****************************************************************************/

void decimate(long double *in, long double *out, float sr1, float sr2, int n1, int n2) {

       logger("Start decimate",0.0);

       int i, j, ii, n, jj;
       int step;
       long double out1[n1];
       long double a[3],b[3];

       logger("    n1",n1);
       // intialize out
       for (i=0;i<n2;i++) out[i] = 0.0;

       // butter worth filter with 8 Hz sample rate and 0.5 Hz cut off
       if (sr1==0.125) {
           logger("    Butter worth filter with 8 Hz sample rate, 0.5 Hz cut off",0.0);
           a[0] = 1.000000000000000;
           a[1] = -1.454243586251585;
           a[2] = 0.574061915083955;
           b[0] = 0.029954582208092;
           b[1] = 0.059909164416185;
           b[2] = 0.029954582208092;
       }
       // butter worth filter with 64 Hz sample rate and 2 Hz cut off
       if (sr1==0.015625) {
           logger("    Butter worth filter with 64 Hz sample rate, 2 Hz cut off",0.0);
           a[0] = 1.000000000000000;
           a[1] = -1.723776172762509;
           a[2] = 0.757546944478829;
           b[0] = 0.008442692929080;
           b[1] = 0.016885385858160;
           b[2] = 0.008442692929080;
       }
       if (!floorf(sr2/sr1==sr2/sr1)) {
              debug("Error: step a non integer",0.0);
              return;
       }  

       out1[0] = in[0];
       out1[1] = in[1];
       for (i=2; i<n1; i++){
            out1[i] = b[0]*in[i] +  b[1]*in[i-1] + b[2]*in[i-2] 
                                - a[1]*out1[i-1] - a[2]*out1[i-2];
       } 
       
       step = sr2/sr1;
       logger("    step",step);
       for (i=0, j=0; i<n1; i+=step,j++){
              if (j>=n2) {
                  fprintf(stderr,"ERROR: out of bounds in decimate. Exiting.\n");
                  exit(0);
              }
              out[j] = out1[i];
       } 

       logger("End decimate",0.0);
       return;
}

