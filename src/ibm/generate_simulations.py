#!/usr/bin/env python

import numpy as np
import math

mu_g = 0.01
wmin = 0
omega2 = [ 0.7 ]
mu_m_g = [ 0, 0.01 ]
mu_m_e = [ 0, 0.01 ]
mu_m_m = [ 0, 0.01 ]
mu_b = [ 0, 0.01 ]
sigma_e = [ 1.0 ]
sigma_ksi = 0.01


mu_m_g = [ 0 ]
mu_m_e = [ 0 ]
mu_m_m = [ 0, 0.01 ]
mu_b = [ 0.0 ]

t_change = 5000

step = 30
freq = list(np.arange(0, math.pi + math.pi/step, math.pi/step))
#freq = [ 0.5, math.pi - 0.5 ]

freq = [freq[3]]

step = 10.0 
min = 2.0
max = 5.0
intercept_t1 = list(np.arange(min,max + (max-min)/step, (max-min)/step))
#intercept_t1 = list(range(50, 200, 10))

#intercept_t1 = [ 6 ]


tau = [ 0.25 ]
sdmu = 0.02

ampl = 2.0

replicates = 1
ctr = 0 
exe = "./xm_sin_change"


for rep_i in range(0, replicates):
    for mu_m_g_i in mu_m_g:
        for mu_m_e_i in mu_m_e:
            for mu_m_m_i in mu_m_m:
                for mu_b_i in mu_b:
                    for sigma_e_i in sigma_e:
                        for freq_i in freq:
                            for omega2_i in omega2:
                                for tau_i in tau:
                                    for intercept_t1_i in intercept_t1:

                                        print("echo " + str(ctr))
                                        ctr+=1

                                        print(exe + " " 
                                                + str(mu_g) + " " 
                                                + str(mu_m_g_i) + " "
                                                + str(mu_m_e_i) + " "
                                                + str(mu_m_m_i) + " "
                                                + str(mu_b_i) + " "
                                                + str(sdmu) + " "
                                                + str(sigma_e_i) + " "
                                                + str(sigma_ksi) + " "
                                                + str(wmin) + " "
                                                + str(0) + " "
                                                + str(omega2_i) + " "
                                                + str(100) + " "
                                                + str(100) + " "
                                                + str(100) + " "
                                                + str(100) + " "
                                                + str(tau_i) + " "
                                                + str(0) + " " # intercept t0
                                                + str(freq_i) + " " # rate t0
                                                + str(ampl) + " " # ampl t0
                                                + str(intercept_t1_i) + " " # intercept t1
                                                + str(freq_i) + " " # rate t1
                                                + str(ampl) + " " # ampl t1
                                                + str(t_change) + " " # ampl t1
                                                )

