import brainpy as bp
import brainpy.math as bm

import numpy as np
import matplotlib.pyplot as plt

# define HH model class
class HH_neurons(bp.dyn.NeuGroup):
    # initialization
    def __init__(self, size, 
                        ENa = 50., gNa = 120., 
                        EK = -77., gK = 36., 
                        EL = -54.387, gL = 0.03,
                        V_th = 20., C = 1., T = 6.3):
        super().__init__(size=size)
        
        # parameters
        self.ENa = ENa
        self.gNa = gNa
        self.EK = EK
        self.gK = gK
        self.EL = EL
        self.gL = gL
        self.V_th = V_th
        self.C = C
        self.T_base = 6.3
        self.Q10 = 3.
        self.phi = self.Q10 ** ((T - self.T_base)/10)
        
        # variables
        self.V = bm.Variable(-70.68 * bm.ones(self.num))
        self.m = bm.Variable(0.0266 * bm.ones(self.num))
        self.h = bm.Variable(0.772 * bm.ones(self.num))
        self.n = bm.Variable(0.235 * bm.ones(self.num))
        self.input = bm.Variable(bm.zeros(self.num))
        self.spike = bm.Variable(bm.zeros(self.num, dtype=bool))
        self.t_last_spike = bm.Variable(bm.ones(self.num) * -1e7)
        
        # integral funtion
        self.integral = bp.odeint(f = self.derivative, method='exp_auto')

    # Derivative funtion
    @property
    def derivative(self):
        return bp.JointEq(self.dV, self.dm, self.dh, self.dn)

    def dm(self, m, t, V):
        alpha = 0.1 * (V + 40) / (1 - bm.exp(-(V + 40) / 10))
        beta = 4.0 * bm.exp(-(V + 65) / 18)
        dmdt = alpha * (1 - m) - beta * m
        return self.phi * dmdt

    def dh(self, h, t, V):
        alpha = 0.07 * bm.exp(-(V + 65) / 20)
        beta = 1 / (1 + bm.exp(-(V + 35) / 10))
        dhdt = alpha * (1 - h) - beta * h
        return self.phi * dhdt

    def dn(self, n, t, V):
        alpha = 0.01 * (V + 55) / (1 - bm.exp(-(V + 55) / 10))
        beta = 0.125 * bm.exp(-(V + 65) / 80)
        dndt = alpha * (1 - n) - beta * n
        return self.phi * dndt

    def dV(self, V, t, m, h, n):
        I_Na = (self.gNa * m ** 3 * h) * (V - self.ENa)
        I_K = (self.gK * n ** 4) * (V - self.EK)
        I_leak = self.gL * (V - self.EL)
        dVdt = (-I_Na - I_K - I_leak + self.input) / self.C
        return dVdt

    # update
    def update(self):
        t = bp.share['t']
        dt = bp.share['dt']
    
        V, m, h, n = self.integral(self.V, self.m, self.h, self.n, t, dt=dt)
    
        self.spike.value = bm.logical_and(self.V < self.V_th, V >= self.V_th)
    
        self.t_last_spike.value = bm.where(self.spike, t, self.t_last_spike)
    
        self.V.value = V
        self.m.value = m
        self.h.value = h
        self.n.value = n
    
        self.input[:] = 0

current, length = bp.inputs.section_input(values=[0., bm.asarray([1.,2.,4.,8.,10.,15.]),0.],
                                          durations=[10,2,25],
                                          return_length=True)
hh_neurons = HH_neurons(current.shape[1])

runner = bp.dyn.DSRunner(hh_neurons, monitors = ['V','m','h','n'], inputs = ['input',current,'iter'])

runner.run(length)

bp.visualize.line_plot(runner.mon.ts, runner.mon.V, ylabel='V(mV)', plot_ids=np.arange(current.shape[1]))

plt.plot(runner.mon.ts, bm.where(current[:,-1]>0,10,0) - 90)
plt.savefig('1.pdf')
plt.clf()

plt.plot(runner.mon.ts, runner.mon.m[:,-1])
plt.plot(runner.mon.ts, runner.mon.h[:,-1])
plt.plot(runner.mon.ts, runner.mon.n[:,-1])
plt.legend(['m','h','n'])
plt.xlabel('Time(ms)')
plt.savefig('2.pdf')