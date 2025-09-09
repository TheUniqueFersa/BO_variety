import matplotlib.pyplot as plt
import math

# -------- Datos inversa (A) --------
IzA_mA = [0.05,0.1,0.5,1,5,10,15,20,30,50]
VzA_V  = [5.29,5.39,5.45,5.45,5.47,5.49,5.50,5.52,5.55,5.60]
VnegA  = [-v for v in VzA_V]
InegA  = [-i*1e-3 for i in IzA_mA]   # A

# -------- Datos inversa (B) --------
IzB_mA = [0.05,0.1,0.5,1,5,10,15,20,30,50]
VzB_V  = [5.481,5.499,5.54,5.559,5.60,5.618,5.628,5.636,5.646,5.66]
VnegB  = [-v for v in VzB_V]
InegB  = [-i*1e-3 for i in IzB_mA]  # A

def plot_zoom_neg(ax, V_neg, I_neg, title, vcolor='blue'):
    vmin, vmax = min(V_neg), max(V_neg)
    imin, imax = min(I_neg), max(I_neg)

    # Mapear a [-1,0] para ocupar toda el área
    xz = lambda v: (v - vmin)/(vmax - vmin) - 1.0
    yz = lambda i: (i - imin)/(imax - imin) - 1.0

    X = [xz(v) for v in V_neg]
    Y = [yz(i) for i in I_neg]
    X, Y = zip(*sorted(zip(X, Y)))

    ax.plot(X, Y, '-o', color=vcolor,lw=2.5, ms=8, label='Zona inversa')

    # Ticks X: paso 0.05 V dentro del rango real
    step = 0.05
    t = math.ceil(vmin/step)*step
    ticksV = []
    while t <= vmax + 1e-12:
        ticksV.append(round(t, 2))
        t += step
    ax.set_xticks([xz(t) for t in ticksV])
    ax.set_xticklabels([f"{t:.2f} V" for t in ticksV])

    # Ticks Y en mA dentro del rango real
    tick_mA_candidates = [-50,-30,-20,-10,-5,-1,-0.5,-0.1,-0.05]
    ticks_mA = [t for t in tick_mA_candidates if (imin*1e3) <= t <= (imax*1e3)]
    ax.set_yticks([yz(t*1e-3) for t in ticks_mA])
    ax.set_yticklabels([f"{t:g} mA" for t in ticks_mA])

    ax.set_xlim(-1.02, 0.02)
    ax.set_ylim(-1.02, 0.02)
    ax.grid(True, ls='--', alpha=0.5)
    ax.set_title(title)
    ax.set_xlabel("Voltaje Vd (V)")
    ax.set_ylabel("Corriente Id (mA)")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
plot_zoom_neg(axes[0], VnegA, InegA, "Datos prácticos", 'orange')
plot_zoom_neg(axes[1], VnegB, InegB, "Datos simulados")
plt.tight_layout()
plt.show()
