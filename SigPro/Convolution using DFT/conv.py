"""
Author      : G Abhiram <gabhiram@smail.iitm.ac.in>
Date Created: May 14, 2022
Description : Convolution using DSP
• To use Linear and Circular Convolution to find the output of a low pass FIR filter for a
given input.
• To see how linear convolution can be interpreted as circular convolution with aliasing
• To analyse the correlation of the Zadoff-Chu sequence
"""
import numpy as np
import scipy.signal as sp
from pylab import *
import csv

figNum = 0
def signal(t, x, figTitle=None, style='b-', blockFig=False, showFig=False, saveFig=True, stemPlot=True, xLimit=None, yLimit=None, xLabel=r"$n\ \to$", yLabel=None):
    global figNum
    plt.figure(figNum)
    plt.title(figTitle)
    plt.grid()
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    if(stemPlot):
        plt.stem(t, x, linefmt='b-', markerfmt='bo')
    else:
        plt.plot(t, x, style)
    if(xLimit):
        plt.xlim(xLimit)
    if(yLimit):
        plt.ylim(yLimit)
    if(saveFig):
        plt.savefig(str(figNum)+".png")
    if(showFig):
        plt.show(block=blockFig)
    figNum+=1

def spectrum(w, Y, figTitle=None, magStyle='b-', phaseStyle='g', xLimit=None, yLimit=None, showFig=False, saveFig=True, blockFig=False, type="Y"):
    global figNum
    plt.figure(figNum)
    plt.suptitle(figTitle)
    plt.subplot(211)
    plt.grid()
    plt.plot(w, abs(Y), magStyle, lw=2)
    plt.ylabel(r"$\| "+type+"\|$")
    if (xLimit):
        plt.xlim(xLimit)
    if (yLimit):
        plt.ylim(yLimit)
    plt.subplot(212)
    plt.grid()
    plt.plot(w, np.angle(Y), phaseStyle, lw=2)
    plt.xlim(xLimit)
    plt.ylabel(r"$\angle "+type+"$")
    plt.xlabel(r"$\omega\ \to$")

    if(saveFig):
        plt.savefig(str(figNum)+".png")
    if(showFig):
        plt.show(block=blockFig)
    figNum+=1

#Parts 1 and 2: Plotting the Magnitude and Phase Response of the FIR filter whose coefficients are in h.csv
filter = np.genfromtxt("h.csv")
signal(range(len(filter)), filter, "FIR Filter ($h[n]$)", showFig=True, yLabel=r"$h[n]$")
w, H = sp.freqz(filter, 1)
spectrum(w, H, "Frequency Response of FIR Filter ($H(e^{j\omega}))$", type="H", showFig=True)

# Question 3: Plotting the input signal x[n]
n = np.linspace(1, 2**10, 2**10)
x = np.cos(0.2*pi*n) + np.cos(0.85*pi*n)
signal(n, x, figTitle="$x[n] = cos(0.2\pi n) + cos(0.85\pi n)$", xLimit=[0, 50], showFig=True, yLabel=r"$x[n]$")

#Question 4: Linear Convolution of x[n] and h[n]
y = np.convolve(x, filter)
signal(list(range(len(y))), y, figTitle=r"$y[n] = x[n]\ast h[n]$", xLimit=[0, 100], showFig=True, yLabel=r"$y[n]$")

#4(b)
y1 =  convolve(x,filter)
figure()
plot(range(len(n)+len(filter)-1),y1,'r')
xlabel(r'$n\rightarrow$',size=15)
ylabel(r'$y\rightarrow$',size=15)
title(r'CT plot of output $y=x*h$')
xlim([1,100])
savefig("CT Output Linear Convolution.png")

#Question 5:
numZeros = len(x)-len(filter)
y = np.fft.ifft(np.fft.fft(x)*np.fft.fft(np.concatenate((filter, np.zeros(numZeros,)))))
signal(list(range(len(y))), y, figTitle=r"$y[n] = x[n]\otimes h[n]$ (N = 1024)", xLimit=[0, 100], showFig=True, yLabel=r"$y[n]$")

#Question 6:
XZeroes = len(filter) - 1
Hzeroes = len(x) - 1
paddedX = np.concatenate((x, np.zeros(XZeroes,)))
paddedH = np.concatenate((filter, np.zeros(Hzeroes,)))
y = np.fft.ifft(np.fft.fft(paddedX)*np.fft.fft(paddedH))
signal(list(range(len(y))), y, figTitle=r"$y[n] = x[n]\otimes h[n]$ (N = 1034), with zero-padding of $x[n]$ and $h[n]$", xLimit=[0, 100], showFig=True, yLabel=r"$y[n]$")

#Question 7:
file2 = "x1.csv"
f1 = open("x1.csv")
zChu = f1.readlines()
zChu  = asarray([complex(i[:-1].replace('i','j')) for i in zChu],dtype = 'complex')

spectrum(list(range(len(zChu))), np.asarray(zChu, dtype=np.complex), r"Zadoff-Chu Sequence", phaseStyle='r-', showFig=True, type=r"zChu[n]", yLimit=[-0.5, 1.5])
zChuShifted = np.roll(zChu, 5)
y = np.fft.ifftshift(np.correlate(zChuShifted, zChu, "full"))
figure(9)
plot(abs(y))
xlabel("$n$")
ylabel("$cor[n]$", size = 12)
title("Zadoff-Chu correlation with shift of 5")
xlim([0,20])
grid(True)
savefig('8.png', dpi=1000)
