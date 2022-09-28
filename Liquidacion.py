import tkinter as tk
from tkinter import StringVar, messagebox


def liquidar():
    sb = float(in_sueldo_bruto.get())
    if sb == 0:
        messagebox.showerror("Error", "Ingrese Sueldo bruto")

    c_horas_extra = int(in_horas_extra.get()) * 0.01 * sb
    c_antig = int(in_antig.get()) * 0.03 * sb
    ing_brut = sb + c_horas_extra + c_antig
    d_jub = 0.11 * ing_brut

    mult_ganancias = 0
    if ing_brut > 777000:
        mult_ganancias = 0.25
    elif ing_brut > 583000:
        mult_ganancias = 0.23
    elif ing_brut > 388000:
        mult_ganancias = 0.19
    elif ing_brut > 291000:
        mult_ganancias = 0.15
    elif ing_brut > 194000:
        mult_ganancias = 0.12
    elif ing_brut > 97000:
        mult_ganancias = 0.09

    d_gan = mult_ganancias * ing_brut

    out_sueldo_bruto.config(state="normal")
    out_sueldo_bruto.delete(0, tk.END)
    out_sueldo_bruto.insert(0, round(sb, 1))
    out_sueldo_bruto.config(state="readonly")

    out_horas_extra.config(state="normal")
    out_horas_extra.delete(0, tk.END)
    out_horas_extra.insert(0, round(c_horas_extra, 1))
    out_horas_extra.config(state="readonly")

    out_antig.config(state="normal")
    out_antig.delete(0, tk.END)
    out_antig.insert(0, round(c_antig, 1))
    out_antig.config(state="readonly")

    out_jub.config(state="normal")
    out_jub.delete(0, tk.END)
    out_jub.insert(0, round(-d_jub, 1))
    out_jub.config(state="readonly")

    out_gan.config(state="normal")
    out_gan.delete(0, tk.END)
    out_gan.insert(0, round(-d_gan, 1))
    out_gan.config(state="readonly")

    out_neto.config(state="normal")
    out_neto.delete(0, tk.END)
    out_neto.insert(0, round(ing_brut - d_jub - d_gan, 1))
    out_neto.config(state="readonly")


def reset():
    in_sueldo_bruto.set("")
    in_horas_extra.set("")
    in_antig.set("")


# Configure window
root = tk.Tk()
root.title("CINNAMON (PAY)-ROLL")
root.config(width=350, height=460)

# Desc label
tk.Label(root, text="- COMPLETAR LOS PRIMEROS TRES CAMPOS -", fg="green").place(x=55, y=10, width=250, height=25)

# in_sueldo_bruto = tk.StringVar()
# in_horas_extra = tk.StringVar()
# in_antig = tk.StringVar()

# Input labels
tk.Label(root, text="Sueldo bruto:").place(x=30, y=50, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=50, width=120, height=25)
in_sueldo_bruto = tk.Entry(root, justify=tk.CENTER, relief=tk.SUNKEN)
in_sueldo_bruto.place(x=160, y=50, width=120, height=25)

tk.Label(root, text="Horas extras:").place(x=30, y=80, width=120, height=25)
tk.Label(root, text="horas").place(x=240, y=80, width=120, height=25)
in_horas_extra = tk.Entry(root, justify=tk.CENTER)
in_horas_extra.place(x=160, y=80, width=120, height=25)

tk.Label(root, text="Antigüedad:").place(x=30, y=110, width=120, height=25)
tk.Label(root, text="años").place(x=240, y=110, width=120, height=25)
in_antig = tk.Entry(root, justify=tk.CENTER)
in_antig.place(x=160, y=110, width=120, height=25)

# Output labels
tk.Label(root, text="Monto Sueldo bruto:").place(x=30, y=190, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=190, width=120, height=25)
out_sueldo_bruto = tk.Entry(root, justify=tk.CENTER, state='disabled')
out_sueldo_bruto.place(x=160, y=190, width=120, height=25)

tk.Label(root, text="Monto Horas Extras:").place(x=30, y=220, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=220, width=120, height=25)
out_horas_extra = tk.Entry(root, justify=tk.CENTER, state='disabled')
out_horas_extra.place(x=160, y=220, width=120, height=25)

tk.Label(root, text="Monto Antigüedad:").place(x=30, y=250, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=250, width=120, height=25)
out_antig = tk.Entry(root, justify=tk.CENTER, state='disabled')
out_antig.place(x=160, y=250, width=120, height=25)

tk.Label(root, text="Deducción Jubilación:").place(x=30, y=280, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=280, width=120, height=25)
out_jub = tk.Entry(root, justify=tk.CENTER, state='disabled')
out_jub.place(x=160, y=280, width=120, height=25)

tk.Label(root, text="Deducción Ganancias:").place(x=30, y=310, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=310, width=120, height=25)
out_gan = tk.Entry(root, justify=tk.CENTER, state='disabled')
out_gan.place(x=160, y=310, width=120, height=25)

tk.Label(root, text="SUELDO NETO:").place(x=30, y=370, width=120, height=25)
tk.Label(root, text="pesos").place(x=240, y=370, width=120, height=25)
out_neto = tk.Entry(root, fg="blue", justify=tk.CENTER, state='disabled')
out_neto.place(x=160, y=370, width=120, height=25)

# Add buttons
b_liq = tk.Button(root, text="Liquidar", fg='blue', command=liquidar)
b_liq.place(x=160, y=150, width=120, height=25)

b_reset = tk.Button(root, text="Reset", command=reset)
b_reset.place(x=30, y=420, width=120, height=25)

b_exit = tk.Button(root, text="Exit", command=root.quit)
b_exit.place(x=160, y=420, width=120, height=25)

# Colorin, colorado...
root.mainloop()