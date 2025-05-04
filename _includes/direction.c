/******************************************************************************
 * Function: wave_direction_FEM_2hz_accel
 * Purpose: Estimates wave direction using FEM (First-order Extended Maximum 
 *          likelihood Method) from 2Hz accelerometer and motion sensor data
 * 
 * Parameters:
 *   accel[]       - Vertical acceleration time series
 *   pitch[]       - Pitch motion time series
 *   roll[]        - Roll motion time series
 *   return_data   - Struct containing output parameters including:
 *                   - direction_full[] (Full directional spectrum)
 *                   - peak_direction   (Direction at spectral peak)
 *                   - direction        (Mean direction)
 *                   - spread          (Directional spread)
 *                   - ratio           (Directional quality parameter)
 *                   - hs_dir          (Significant wave height)
 * 
 * Returns:
 *   0 on success
 * 
 * Notes:
 *   - Uses cross-spectral analysis between vertical and horizontal motions
 *   - Frequency range defined by rspns_f7 to rspns_f8
 *   - Outputs directional parameters in degrees (0° = waves toward East)
 *   - Implements circular statistics for directional averaging
 *   - Includes spectral analysis using Welch's method
 *   
 * References:
 *   - Extended Maximum Likelihood Method for wave direction analysis
 *   - Circular statistics for directional spread calculation
 * 
 * Output Files:
 *   - roll_spectra.out  - Roll motion spectra
 *   - pitch_spectra.out - Pitch motion spectra
 *   - accel_spectra.out - Acceleration spectra
 *   - direction_full.out - Full directional spectrum
 *   - spread.out        - Directional spread
 * 
 *****************************************************************************/
int wave_direction_FEM_2hz_accel(long double *accel, long double *pitch, long double *roll, struct RETDATA *return_data){

       logger("Start wave_direction_FEM_2hz_accel",0);

       int i,j,peak_id;
       int w=m, ww=2*w, kk=2;
       int st, ed;
       int send_dir[w+1];
       long double df = 1/(ww*dt);
       long double c12[w+1], q12[w+1];
       long double c13[w+1], q13[w+1];
       long double c11[w+1], c22[w+1], c33[w+1];
       long double kd[w+1];
       long double fft_accel[ww], fft_ns[ww], fft_ew[ww];
       long double a1[w+1], b1[w+1];
       long double a2[w+1], b2[w+1];
       long double a3[w+1], b3[w+1];
       long double alpha12[w+1], alpha13[w+1];
       long double aa1[w+1], bb1[w+1], dir[w+1], sprd[w+1], ui[w+1];
       long double aa1s[w+1], bb1s[w+1];
       long double peak = 0, omega, mean_dir;
       long double Hs, c11_sum, dir_mean, ui_mean=0;
       long double ff[w+1];

       // Define ff
       for (i=0;i<w+1;i++) ff[i] = (i/(2.0*m*dt));

       // Initialize variables
       for (i=0;i<w+1;i++){
            c11[i] = 0.0;
            c22[i] = 0.0;
            c33[i] = 0.0;
            c12[i] = 0.0;
            q12[i] = 0.0;
            c13[i] = 0.0;
            q13[i] = 0.0;
            a1[i] = 0.0;
            a2[i] = 0.0;
            a3[i] = 0.0;
            b1[i] = 0.0;
            b2[i] = 0.0;
            b3[i] = 0.0;
            alpha12[i] = 0.0;
            alpha13[i] = 0.0;
            aa1[i] = 0.0;
            bb1[i] = 0.0;
            dir[i] = 0.0;
            sprd[i] = 0.0;
            send_dir[i] = 0;
       }
       for (i=0;i<ww;i++){
            fft_accel[i] = 0.0;
            fft_ns[i] = 0.0;
            fft_ew[i] = 0.0;
       }
       spctrm(roll,fft_ew,w,kk,n_spec,(float)dt);
       spctrm(pitch,fft_ns,w,kk,n_spec,(float)dt);
       spctrm(accel,fft_accel,w,kk,n_spec,(float)dt);
       print2out(fft_ew,ww,"out/roll_spectra.out",ido_rs);
       print2out(fft_ns,ww,"out/pitch_spectra.out",ido_ps);
       print2out(fft_accel,ww,"out/accel_spectra.out",ido_hs);

       // auto / cross correlations
       for (i=0,j=0; i<ww; i+=2,j++){
            if (j>=w+1) {
                fprintf(stderr,"ERROR: out of bounds in wave_direction_FEM_2hz. Exiting.\n");
                exit(0);
            }
            a1[j] = fft_accel[i];
            a2[j] = fft_ns[i];
            a3[j] = fft_ew[i]; 
       }
       a1[w] = fft_accel[ww-1];
       a2[w] = fft_ns[ww-1];
       a3[w] = fft_ew[ww-1];

       b1[0] = 0;
       b1[1] = 0;
       b2[0] = 0;
       b2[1] = 0;
       b3[0] = 0;
       b3[1] = 0;
       for (i=3,j=2; i<ww; i+=2,j++){
            if (j>=w+1) {
                fprintf(stderr,"ERROR: out of bounds in wave_direction_FEM_2hz. Exiting.\n");
                exit(0);
            }
            b1[j] = fft_accel[i];
            b2[j] = fft_ns[i];
            b3[j] = fft_ew[i]; 
       }
       b1[w] = 0;
       b2[w] = 0;
       b3[w] = 0;

       // Find range for directional analysis
       for (i = 0; i<w+1; i++) {
            if (ff[i] > rspns_f7) {
                st = i;
                break;
            }
       }
       for (i = 0; i<w+1; i++) {
            if (ff[i] > rspns_f8) {
                ed = i;
                break;
            }
       }

       c11_sum = 0;
       dir_mean = 0;
       Hs = 0;
       for (i = 1; i<m+1; i++){ 
            omega = (2.0*pi*ff[i])*(2.0*pi*ff[i]);
            c12[i] = a1[i]*a2[i]/omega + b1[i]*b2[i]/omega;
            q12[i] = a1[i]*b2[i]/omega - b1[i]*a2[i]/omega;
            c13[i] = a1[i]*a3[i]/omega + b1[i]*b3[i]/omega;
            q13[i] = a1[i]*b3[i]/omega - b1[i]*a3[i]/omega;
            c11[i] = a1[i]*a1[i]/(omega*omega) + b1[i]*b1[i]/(omega*omega);
            c22[i] = (a2[i]*a2[i] + b2[i]*b2[i]);
            c33[i] = (a3[i]*a3[i] + b3[i]*b3[i]);
            alpha12[i] = atan2(c12[i],q12[i]);
            alpha13[i] = atan2(c13[i],q13[i]);
            aa1[i] = (c12[i]*sin(alpha12[i]) + q12[i]*cos(alpha12[i]))/sqrt(c11[i]*(c22[i]+c33[i]));
            bb1[i] = (c13[i]*sin(alpha13[i]) + q13[i]*cos(alpha13[i]))/sqrt(c11[i]*(c22[i]+c33[i]));
            kd[i] = sqrt((c22[i]+c33[i])/c11[i]);
            aa1s[i] = q12[i]/(kd[i]*c11[i]);
            bb1s[i] = q13[i]/(kd[i]*c11[i]);
            // note that 0 deg is for waves headed towards positive x (EAST, right hand system)
            dir[i] = atan2(bb1[i],aa1[i]);
            ui[i] = sqrt(aa1s[i]*aa1s[i] + bb1s[i]*bb1s[i]);
            sprd[i] = sqrt(2.0*(1.0-ui[i])); //circular spread (Degrees) from Doble
            return_data->direction_full[i] = round(dir[i]*1800.0/pi);
            if ((i >= st) && (i < ed)) {
                 c11_sum += c11[i];
                 dir_mean += dir[i];
                 ui_mean += ui[i];
                 if (peak<=c11[i]) {
                     peak = c11[i];
                     peak_id = i;
                 }
            }
       }
       return_data->peak_direction = dir[peak_id];
       return_data->direction = dir_mean/(ed-st);
       return_data->spread = sprd[peak_id];
       return_data->ratio = ui_mean/(ed-st);
       //return_data->ratio =sqrt(c11[peak_id]/(c22[peak_id]/kd[peak_id] + c33[peak_id]/kd[peak_id]));

       // Significant wave height
       return_data->hs_dir = 4.0*sqrt(c11_sum);

       print2out(c11,w+1,"out/c11.out",ido_od);
       print2out(dir,w+1,"out/direction_full.out",ido_od);
       print2out(sprd,w+1,"out/spread.out",ido_od);
       print2out(aa1,w+1,"out/aa1.out",ido_od);
       print2out(bb1,w+1,"out/bb1.out",ido_od);

       logger("End wave_direction_FEM_2hz",0);
       return(0);
}
