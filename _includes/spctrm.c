/******************************************************************************
 * Function: spctrm_psd
 * Purpose: Calculates Power Spectral Density using Welch's method with
 *          overlapping segments and 10% cosine tapering
 * 
 * Parameters:
 *   disp[] - Input displacement time series data
 *   p[]    - Output array for power spectral density values
 *   m      - Half the segment length (full segment = 2m)
 *   k      - Number of segments to average (determines overlap)
 * 
 * Returns:
 *   0 on success
 * 
 * Notes:
 *   - Applies detrending and demeaning to each segment
 *   - Uses 10% cosine taper window
 *   - Includes overlap processing for improved spectral estimates
 *   - Normalizes output by window power and number of segments
 * 
 *****************************************************************************/
int spctrm_psd(long double disp[], long double p[], int m, int k) {

        FILE *id;
        int i=0,ii=0,j=0,count=0;
        int mm=2*m;
        int gamma;
        int cl = 1;
        float r=0.0;
        long double win[mm], sumw=0;
        long double dp[mm], psd[2*k][m+1];
        long double alpha, beta, t1;
        long double w1[mm];


        // Intialize 
        for (i=0;i<mm;i++) dp[i] = 0.0;
        for (i=0;i<m+1;i++) {
             for(j=0;j<2*k;j++) psd[j][i] = 0.0;
             p[i] = 0.0;
        }

        // define 10% cosine taper
        gamma = 5; t1 = m-m/gamma; alpha = 2.0*3.14159265*gamma/mm;
        if (gamma % 2 == 0) beta = 3.14159265; else beta = 0;
        for (i=0;i<m;i++) {
             if (i<t1) win[i] = 1;
             else win[i] = 0.5*(1 + cos(alpha*i + beta)); 
        }
        for (i=m;i<mm;i++) win[i] = win[i-m]; 
        for (i=0;i<m;i++) win[i] = win[mm-1-i];
        for (i=0;i<mm;i++) sumw += pow(win[i],2.0);
        for (i=0;i<mm;i++) if(isnan(win[i])) debug("nan",i);

        for (j=0,count=0; j<2*k; j++, count+=m) {
             for (i=0;i<mm;i++) {
                  dp[i] = disp[count+i];
                  demean(dp,i);
                  trend_removal(dp,mm);
                  demean(dp,i);
                  w1[i] = win[i]*dp[i];
             }
             realft(w1,mm,1);
             psd[j][0] = pow(w1[0],2); psd[j][m] = pow(w1[1],2);
             for (i=2,ii=1; i<mm-1; i+=2,ii++) {
                  if (ii>=m+1) {
                      fprintf(stderr,"ERROR: out of bounds in spctrm_psd. Exiting.\n");
                      exit(0);
                  }
                  if (i>=2*m-1) {
                      fprintf(stderr,"ERROR: out of bounds in spctrm_psd. Exiting.\n");
                      exit(0);
                  }
                  psd[j][ii] = 2*(pow(w1[i],2) + pow(w1[i+1],2)); 
             }
        }

        for (i=0; i<m+1; i++) {
             p[i]=0.0;
             for (j=0; j<2*k; j++) p[i]+=psd[j][i];
             p[i] /= (2.0*k*mm*sumw);
        }

        return(0);
}
