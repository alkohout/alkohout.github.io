
/******************************************************************************
 * Function: quality_control_accel
 * Purpose: Performs quality control checks on accelerometer data including
 *          spike detection, flat signal detection, and statistical validation
 * 
 * Parameters:
 *   data_raw    - Struct containing raw accelerometer data:
 *                 - accel_raw_kist (Kistler accelerometer)
 *                 - accel_raw_x/y/z (IMU accelerometer axes)
 *   return_data - Struct containing quality flags and metrics:
 *                 - qflg_kist (Kistler quality flag)
 *                 - qflg_accel (IMU quality flag)
 *                 - qflg_pkist (Kistler percentage flag)
 * 
 * Returns:
 *   void
 * 
 * Quality Checks:
 *   1. Flat Signal Detection
 *      - Identifies unresponsive periods
 *      - Threshold: 0.5
 *      - Applies patch correction
 *   
 *   2. Spike Detection
 *      - Kistler: 10 iterations with nstd_kist threshold
 *      - IMU: Single pass with nstd_imu threshold
 *      - Applies patch correction after detection
 *   
 *   3. Statistical Validation
 *      - Performs basic statistical tests
 *      - Sets quality flags based on results
 * 
 * Output Metrics:
 *   - Percentage of compromised data
 *   - Counts of detected spikes and flat periods
 *   - Separate quality flags for Kistler and IMU data
 * 
 * Notes:
 *   - Implements different thresholds for Kistler and IMU
 *   - Patches detected issues in-place
 *   - Generates detailed quality control log if PRINT_OUTPUT defined
 * 
 *****************************************************************************/
void quality_control_accel(struct DATARAW *data_raw, struct RETDATA *return_data){

    logger("Start quality_control_accel",0.0);

    int i, r;
    int t1 = 0;
    int n_flat_k=0,n_flat_x=0, n_flat_y=0, n_flat_z=0; 
    int max_flat_k=0, max_flat_x=0, max_flat_y=0, max_flat_z=0;
    int n_spike_k=0, n_spike_x=0, n_spike_y=0, n_spike_z=0; 
    int max_spike_k=0, max_spike_x=0, max_spike_y=0, max_spike_z=0;
    int qflg_k=0,qflg_x=0,qflg_y=0,qflg_z=0;
    int temp_n, temp_max;

    // Flat
    qflg_k = flat(data_raw->accel_raw_kist,&n_flat_k,&max_flat_k,0.5,n_raw); 
    if (qflg_k == 1) return_data->qflg_kist = 1;
    patch(data_raw->accel_raw_kist,n_raw);
    qflg_x = flat(data_raw->accel_raw_x,&n_flat_x,&max_flat_x,0.5,n_raw); 
    patch(data_raw->accel_raw_x,n_raw);
    qflg_y = flat(data_raw->accel_raw_y,&n_flat_y,&max_flat_y,0.5,n_raw); 
    patch(data_raw->accel_raw_y,n_raw);
    qflg_z = flat(data_raw->accel_raw_z,&n_flat_z,&max_flat_z,0.5,n_raw); 
    patch(data_raw->accel_raw_z,n_raw);

    // Despike 
    // run despike on Kistler several times to remove all spikes
    for (i=0;i<10;i++){
         despike(data_raw->accel_raw_kist,&temp_n,&temp_max,n_raw,nstd_kist); 
         patch(data_raw->accel_raw_kist,n_raw);
         n_spike_k = n_spike_k + temp_n;
         max_spike_k = max_spike_k + temp_max;
    }
    despike(data_raw->accel_raw_x,&n_spike_x,&max_spike_x,n_raw,nstd_imu); 
    patch(data_raw->accel_raw_x,n_raw);
    despike(data_raw->accel_raw_y,&n_spike_y,&max_spike_y,n_raw,nstd_imu); 
    patch(data_raw->accel_raw_y,n_raw);
    despike(data_raw->accel_raw_z,&n_spike_z,&max_spike_z,n_raw,nstd_imu); 
    patch(data_raw->accel_raw_z,n_raw);

    // Test stats
    if (return_data->qflg_kist == 0) {
        return_data->qflg_kist = test_stats(data_raw->accel_raw_kist,n_raw);
    }
    r = test_stats(data_raw->accel_raw_x,n_raw);
    if (r == 1) return_data->qflg_accel = 100;
    r = test_stats(data_raw->accel_raw_y,n_raw);
    if (r == 1) return_data->qflg_accel = 100;
    r = test_stats(data_raw->accel_raw_z,n_raw);
    if (r == 1) return_data->qflg_accel = 100;
        
    // Return flags
    if (return_data->qflg_accel <100) {
        return_data->qflg_accel = (int)100*(n_flat_x + n_spike_x + n_flat_y + n_spike_y + n_flat_z + n_spike_z)/(n_raw*3);
    }
    return_data->qflg_pkist = (int)100*(n_flat_k + n_spike_k)/(n_raw);

    // Print  
    #ifdef PRINT_OUTPUT 
    fprintf(ido_oqc,"ACCEL QUALITY FLAGS\n");
    fprintf(ido_oqc,"Quality flag x = %d\n", qflg_x);
    fprintf(ido_oqc,"Quality flag y = %d\n", qflg_y);
    fprintf(ido_oqc,"Quality flag z = %d\n", qflg_z);
    fprintf(ido_oqc,"Number of unresponsive x = %d\n",n_flat_x);
    fprintf(ido_oqc,"Number of unresponsive y = %d\n",n_flat_y);
    fprintf(ido_oqc,"Number of unresponsive z = %d\n",n_flat_z);
    fprintf(ido_oqc,"Number of spikes x = %d\n",n_spike_x);///(long double)n_raw);
    fprintf(ido_oqc,"Number of spikes y = %d\n",n_spike_y);///(long double)n_raw);
    fprintf(ido_oqc,"Number of spikes z = %d\n",n_spike_z);///(long double)n_raw);
    #endif
    
    logger("End quality_control_accel",0.0);

    return ;
}
