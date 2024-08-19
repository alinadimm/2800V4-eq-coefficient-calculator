import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pyperclip


group_names = {
    'Group A': 'الف - سیستم دیوارهای باربر',
    'Group B': 'ب - سیستم قاب ساختمانی',
    'Group C': 'پ - سیستم قاب خمشی',
    'Group D': 'ت - سیستم دوگانه یا ترکیبی',
    'Group E': 'ث - سیستم کنسولی'
}

framing_groups = {
    'الف - سیستم دیوارهای باربر': {
        'دیوار برشی بتن آرمه ویژه': (5, 2.5, 5, 50),
        'دیوارهای برشی بتن‌آرمه متوسط': (4, 2.5, 4, 50),
        'دیوارهای برشی بتن‌آرمه معمولی': (3.5, 2.5, 3.5, None),
        'دیوارهای برشی با مصالح بنایی مسلح': (3, 2.5, 3, 15),
        'دیوارهای متشکل از قاب‌های سبک فولادی سرد نورد و مهارهای تسمه فولادی': (4, 2, 3.5, 15),
        'دیوارهای متشکل از قاب سبک فولادی سرد نورد و صفحات پوشش فولادی': (5.5, 3, 4, 15),
        'دیوارهای بتن پاششی سه‌ بعدی': (3, 2, 3, 10)
    },
    'ب - سیستم قاب ساختمانی': {
        'دیوارهای برشی بتن آرمه ویژه': (6, 2.5, 5, 50),
        'دیوارهای برشی بتن‌آرمه متوسط': (5, 2.5, 4, 35),
        'دیوار برشی بتن‌آرمه معمولی': (4, 2.5, 3, None),
        'دیوارهای برشی با مصالح بنایی مسلح': (3, 2.5, 2.5, 15),
        'مهاربندی واگرای ویژه فولادی': (7, 2, 4, 50),
        'مهاربندی کمانش تاب': (7, 2.5, 5, 50),
        'مهابندی همگرای معمولی فولادی': (3.5, 2, 3.5, 15),
        'مهاربندی همگرای ویژه فولادی': (5.5, 2, 5, 50)
    },
    'پ - سیستم قاب خمشی': {
        'قاب خمشی بتن‌آرمه ویژه': (7.5, 3, 5.5, 200),
        'قاب خمشی بتن‌آرمه متوسط': (5, 3, 4.5, 35),
        'قاب خمشی بتن‌آرمه معمولی': (3, 3, 2.5, None),
        'قاب خمشی فولادی ویژه': (7.5, 3, 5.5, 200),
        'قاب خمشی فولادی متوسط': (5, 3, 4, 50),
        'قاب خمشی فولادی معمولی': (3.5, 3, 3, None)
    },
    'ت - سیستم دوگانه یا ترکیبی': {
        'قاب خمشی ویژه (فولادی یا بتنی) + دیوارهای برشی بتن‌آرمه ویژه': (7.5, 2.5, 5.5, 200),
        'قاب خمشی بتن‌آرمه متوسط + دیوار برشی بتن‌آرمه ویژه': (6.5, 2.5, 5, 70),
        'قاب خمشی بتن‌آرمه متوسط + دیوار برشی بتن‌آرمه متوسط': (6, 2.5, 4.5, 50),
        'قاب خمشی فولادی متوسط + دیوار برشی بتن‌آرمه متوسط': (6, 2.5, 4.5, 50),
        'قاب خمشی فولادی ویژه + مهاربندی واگرای ویژه فولادی': (7.5, 2.5, 4, 200),
        'قاب خمشی فولادی متوسط + مهاربندی واگرای ویژه فولادی': (6, 2.5, 5, 70),
        'قاب خمشی فولادی ویژه + مهاربندی همگرای ویژه فولادی': (7, 2.5, 5.5, 200),
        'قاب خمشی فولادی متوسط + مهاربندی همگرای ویژه فولادی': (6, 2.5, 5, 70)
    },
    'ث - سیستم کنسولی': {
        'سازه‌های فولادی ی بتن‌آرمه ویژه': (2, 1.5, 2, 10)
    }
}

importance_groups = {
    'گروه یک': 1.4,
    'گروه دو': 1.2,
    'گروه سه': 1.0,
    'گروه چهار': 0.8
}

regional_vulnerability_groups = {
    'پهنه با خطر نسبی کم': 0.2,
    'پهنه با خطر نسبی متوسط': 0.25,
    'پهنه با خطر نسبی زیاد': 0.3,
    'پهنه با خطر نسبی خیلی زیاد': 0.35
}


# Soil type data based on A
soil_type_data_low_to_medium_A = {
    'I': (0.1, 0.4, 1.5, 1),
    'II': (0.1, 0.5, 1.5, 1),
    'III': (0.15, 0.7, 1.75, 1.1),
    'IV': (0.15, 1, 2.25, 1.3),
}

soil_type_data_high_to_very_high_A = {
    'I': (0.1, 0.4, 1.5, 1),
    'II': (0.1, 0.5, 1.5, 1),
    'III': (0.15, 0.7, 1.75, 1.1),
    'IV': (0.15, 1, 1.75, 1.1),
}


def on_group_selected(event):
    selected_group = group_var.get()
    framing_systems = framing_groups[selected_group]
    system_var.set('')
    system_menu['menu'].delete(0, 'end')
    font_style = ('B Nazanin', 14)
    for system in framing_systems:
        system_menu['menu'].add_command(label=system, command=tk._setit(system_var, system), font=font_style)


def on_system_selected(*args):
    selected_group = group_var.get()
    selected_system = system_var.get()
    if selected_system:
        Ru, Ω0, Cd, Hm = framing_groups[selected_group][selected_system]
        Ru_label.config(text=f"Rᵤ: {Ru}")
        Ω0_label.config(text=f"Ω₀: {Ω0}")
        Cd_label.config(text=f"Cd: {Cd}")
        Hm_label.config(text=f"Hₘ: {Hm}")
        return Ru

def on_calculation_clicked(event=None):
    selected_group = group_var.get()
    selected_system = system_var.get()
    if selected_system:
        Ru, Ω0, Cd, Hm = framing_groups[selected_group][selected_system]
        Ru_label.config(text=f"Rᵤ: {Ru}")
        Ω0_label.config(text=f"Ω₀: {Ω0}")
        Cd_label.config(text=f"Cd: {Cd}")
        Hm_label.config(text=f"Hₘ: {Hm}")


        # Compare the structure height with Hm
        if structure_height_entry.get():
            structure_height = float(structure_height_entry.get())
            if Hm and structure_height > Hm:
                message_label.config(text="ارتفاع سازه از ارتفاع مجاز این سیستم بیشتر است", fg="red")
            else:
                message_label.config(text="")
        else:
            message_label.config(text="ارتفاع سازه را وارد کنید", fg="red")
   
    
    system_type = system_type_var.get()
    height = float(structure_height_entry.get())
    empirical_T = calculate_empirical_T(system_type, height)
    analytical_T = float(analytical_T_entry.get())
    empirical_T_1_25 = 1.25 * empirical_T
    smaller_T = min(analytical_T, empirical_T_1_25)
    formula = calculate_empirical_T_formula(system_type)
    if analytical_T < empirical_T_1_25:
        formula_label.config(text=f"1.25xTₐ = {formula} = {empirical_T_1_25:.3f}(s) > Tₘ")
    elif analytical_T > empirical_T_1_25:
        formula_label.config(text=f"1.25xTₐ = {formula} = {empirical_T_1_25:.3f}(s) < Tₘ")
    else:
        formula_label.config(text=f"1.25xTₐ = {formula} = {empirical_T_1_25:.3f}(s) = Tₘ")

    selected_A = regional_vulnerability_var.get()
    selected_soil_type = soil_type_var.get()
    if selected_soil_type:
        Nformula=''
        if selected_A in ['پهنه با خطر نسبی کم', 'پهنه با خطر نسبی متوسط']:
            T0, Ts, S, S0 = soil_type_data_low_to_medium_A[selected_soil_type]
            N , formula = N_calculator_low(smaller_T, Ts)
        elif selected_A in ['پهنه با خطر نسبی زیاد', 'پهنه با خطر نسبی خیلی زیاد']:
            T0, Ts, S, S0 = soil_type_data_high_to_very_high_A[selected_soil_type]
            N , Nformula = N_calculator_high(smaller_T, Ts)
        N_label.config(text=f'N = {Nformula} {N:.3f}')
        B1 , B1formula = B1_calculator(smaller_T, T0, Ts, S, S0)   
        B1_label.config(text=f'B₁ = {B1formula} {B1:.3f}')
        B = B1*N
        B_label.config(text=f'B = B₁N = {B:.3f}')
        k, kformula = k_calculator(smaller_T)
        # k_label.config(text=f'K = {kformula} {k:.3f}')
        update_k_button_text(k, kformula) 
        
        selected_I = importance_groups_var.get()
        I_value = importance_groups[selected_I]
        A_value = regional_vulnerability_groups[selected_A]
        Cmin = 0.12*A_value*I_value
        C = A_value*B*I_value/Ru
        
        Cmin_label.config(text=f'C(min) = {Cmin:.3f}')
        if C<= Cmin:
            C_label.config(text=f'C = C(min) = {Cmin:.3f}')
        else: 
            C_label.config(text=f'C = {C:.3f}')
        update_C_button_text(C, Cmin) 
        
def N_calculator_low(T, Ts):
    N = 0
    Nformula = ''
    if T<Ts:
        N=1
        Nformula = ''
    elif Ts<T and T<4:
        N=(0.4)/(4-Ts)*(T-Ts)+1
        Nformula = '(0.4)/(4-Ts)*(T-Ts)+1 ='
    elif T>4:
        N=1.4
        Nformula = ''
    return N, Nformula

def N_calculator_high(T, Ts):
    N = 0
    Nformula = ''
    if T<Ts:
        N=1
        Nformula = ''
    elif Ts<T and T<4:
        N=(0.7)/(4-Ts)*(T-Ts)+1
        Nformula = '(0.7)/(4-Ts)*(T-Ts)+1 ='
    elif T>4:
        N=1.7
        Nformula = ''
    return N, Nformula

def B1_calculator(T, T0, Ts, S, S0):
    B1 = None
    B1formula = ''
    if 0<T and T<T0:
        B1=S0+(S-S0+1)*(T/T0)
        B1formula = 'S₀+(S-S₀+1)*(T/T₀) ='
    elif T0<T and T<Ts:
        B1=S+1
        B1formula ='S+1='
    elif T>Ts:
        B1=(S+1)*(Ts/T)
        B1formula ='(S+1)*(Ts/T) ='
    return B1 , B1formula


def k_calculator(T):
    k = None
    kformula = ''
    if T < 0.5:
        k = 1.0
        kformula = ''
    elif 0.5 <= T <= 2.5:
        k = 0.5 * T + 0.75
        kformula = '0.5 * T + 0.75 ='  
    elif T > 2.5:
        k = 2.0
        kformula = ''
    return k , kformula

def copy_k_to_clipboard():
    system_type = system_type_var.get()
    height = float(structure_height_entry.get())
    empirical_T_125 = 1.25*calculate_empirical_T(system_type, height)
    analytical_T = float(analytical_T_entry.get())
    T = min(empirical_T_125, analytical_T)
    k, kformula = k_calculator(T)
    k_label.config(text=f'K = {kformula} {k:.3f}')
    if k is not None:
        k_formatted = "{:.4f}".format(k)
        pyperclip.copy(str(k_formatted))
        k_copy_message_label.config(text="کپی شد", fg='green')
        root.after(800, lambda: k_copy_message_label.config(text=""))
    else:
        k_copy_message_label.config(text="Vvalue not available", fg='red')

def copy_C_to_clipboard():
    selected_group = group_var.get()
    selected_system = system_var.get()
    Ru, Ω0, Cd, Hm = framing_groups[selected_group][selected_system]
    selected_soil_type = soil_type_var.get()
    system_type = system_type_var.get()
    height = float(structure_height_entry.get())
    empirical_T = calculate_empirical_T(system_type, height)
    analytical_T = float(analytical_T_entry.get())
    empirical_T_1_25 = 1.25 * empirical_T
    smaller_T = min(analytical_T, empirical_T_1_25)
    selected_I = importance_groups_var.get()
    I_value = importance_groups[selected_I]
    selected_A = regional_vulnerability_var.get()
    A_value = regional_vulnerability_groups[selected_A]
    if selected_A in ['پهنه با خطر نسبی کم', 'پهنه با خطر نسبی متوسط']:
        T0, Ts, S, S0 = soil_type_data_low_to_medium_A[selected_soil_type]
        N , formula = N_calculator_low(smaller_T, Ts)
    elif selected_A in ['پهنه با خطر نسبی زیاد', 'پهنه با خطر نسبی خیلی زیاد']:
        T0, Ts, S, S0 = soil_type_data_high_to_very_high_A[selected_soil_type]
        N , Nformula = N_calculator_high(smaller_T, Ts)
    B1 , B1formula = B1_calculator(smaller_T, T0, Ts, S, S0)   
    B = B1*N
    Cmin = 0.12*A_value*I_value
    C = A_value*B*I_value/Ru
    
    if C<= Cmin:
        C = Cmin
    if C is not None:

        C_formatted = "{:.4f}".format(C)
        pyperclip.copy(str(C_formatted))
        C_copy_message_label.config(text="کپی شد", fg='green')
        root.after(800, lambda: C_copy_message_label.config(text=""))
        
        if C<= Cmin:
            C_button.config(text=f'C = C(min) = {Cmin:.3f}')
        else: 
            C_button.config(text=f'C = ABI/Rᵤ = {C:.3f}')
            
    return C , Cmin

def update_k_button_text(k, k_formula):
    k_button.config(text=f'K = {k_formula} {k:.3f}')
    k_label.config(text='')
def update_C_button_text(C, Cmin):
    if C<= Cmin:
        C_button.config(text=f'C = C(min) = {Cmin:.3f}')
    else: 
        C_button.config(text=f'C = {C:.3f}')
    

def calculate_expression(event=None):
    expression = structure_height_entry.get()
    try:
        result = eval(expression)
        structure_height_entry.delete(0, tk.END)
        structure_height_entry.insert(0, str(result))
    except Exception as e:
        print(e)


def on_soil_type_selected(event=None):
    selected_A = regional_vulnerability_var.get()
    selected_soil_type = soil_type_var.get()
    if selected_soil_type:
        if selected_A in ['پهنه با خطر نسبی کم', 'پهنه با خطر نسبی متوسط']:
            T0, Ts, S, S0 = soil_type_data_low_to_medium_A[selected_soil_type]
        else:
            T0, Ts, S, S0 = soil_type_data_high_to_very_high_A[selected_soil_type]

        T0_label.config(text=f"T₀: {T0}")
        Ts_label.config(text=f"Ts: {Ts}")
        S_label.config(text=f"S: {S}")
        S0_label.config(text=f"S₀: {S0}")
    

    
def on_A_selected(event=None):
    selected_A = regional_vulnerability_var.get()
    A_value = regional_vulnerability_groups[selected_A]
    if selected_A:
        A_label.config(text=f'A : {A_value}')
        
def on_I_selected(event=None):
    selected_I = importance_groups_var.get()
    I_value = importance_groups[selected_I]
    if selected_I:
        I_label.config(text=f'I : {I_value}')


def calculate_empirical_T(system_type, height):
    if system_type == 'سیستم قاب خمشی فولادی':
        empirical_T = 0.08 * height ** 0.75
    elif system_type == 'سیستم قاب خمشی فولادی با جداگر میانقابی':
        empirical_T = 0.8 * 0.08 * height ** 0.75
    elif system_type == 'سیستم قاب خمشی بتنی':
        empirical_T = 0.05 * height ** 0.9
    elif system_type == 'سیستم قاب خمشی بتنی با جداگر میانقابی':
        empirical_T = 0.8 * 0.05 * height ** 0.9
    elif system_type == 'سیستم قاب ساختمانی ساده با مهاربند واگرا':
        empirical_T = 0.08 * height ** 0.75
    elif system_type == 'سایر سیستم‌های ساختمانی':
        empirical_T = 0.05 * height ** 0.75
    return empirical_T

def calculate_empirical_T_formula(system_type):
    if system_type == 'سیستم قاب خمشی فولادی':
        return '1.25*0.08*h^(0.75)'
    elif system_type == 'سیستم قاب خمشی فولادی با جداگر میانقابی':
        return '1.25*0.8*0.08*h^(0.75)'
    elif system_type == 'سیستم قاب خمشی بتنی':
        return '1.25*0.05*h^(0.9)'
    elif system_type == 'سیستم قاب خمشی بتنی با جداگر میانقابی':
        return '1.25*0.8*0.05*h^(0.9)'
    elif system_type == 'سیستم قاب ساختمانی ساده با مهاربند واگرا':
        return '1.25*0.08*h^(0.75)'
    elif system_type == 'سایر سیستم‌های ساختمانی':  
        return '1.25*0.05*h^(0.75)'
   


def calculate_emperical_T():
    selected_group = group_var.get()
    selected_height = structure_height_entry.get()

    if selected_group and selected_height:

        empirical_T = calculate_empirical_T(selected_group, float(selected_height))
        T_125 = 1.25 * empirical_T


root = tk.Tk()
root.title("Standard 2800 V4 - Earthquake Coefficient")

custom_font = tkFont.Font(family="Vazir", size=13)
custom_font_Latin = tkFont.Font(family='Segoe UI', size=14)


group_label = tk.Label(root, text="گروه سیستم سازه‌ای", font=custom_font)
group_label.grid(row=0, column=1, padx=10, pady=5, sticky="e")

group_var = tk.StringVar()
group_menu = ttk.Combobox(root, textvariable=group_var, width=50, font=custom_font, justify="right")
group_menu['values'] = list(group_names.values())
group_menu.grid(row=0, column=0, padx=10, pady=5, sticky="e")

group_menu.bind("<<ComboboxSelected>>", on_group_selected)

system_label = tk.Label(root, text="سیستم مقاوم جانبی", font=custom_font)
system_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# system_var = tk.StringVar()
# system_menu = ttk.OptionMenu(root, system_var, "", "")
# system_menu.grid(row=1, column=0, padx=10, pady=5, sticky='e')
# system_menu.configure(width=65)
# system_menu.option_add('*TCombobox*Listbox.font', custom_font)

system_var = tk.StringVar()
system_menu = ttk.OptionMenu(root, system_var, "", "")
system_menu.grid(row=1, column=0, padx=10, pady=5, sticky='e')
system_menu.configure(width=65)
system_menu.option_add('*TCombobox*Listbox.font', custom_font)

# Bind the function to the selection event
system_var.trace_add("write", on_system_selected)

regional_vulnerability_label = tk.Label(root, text="خطر نسبی", font=custom_font)
regional_vulnerability_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

regional_vulnerability_var = tk.StringVar()
regional_vulnerability_menu = ttk.Combobox(root, textvariable=regional_vulnerability_var, width=20, font=custom_font, justify="right")
regional_vulnerability_menu['values'] = list(regional_vulnerability_groups.keys())
regional_vulnerability_menu.grid(row=2, column=0, padx=10, pady=5, sticky="e")
regional_vulnerability_menu.bind("<<ComboboxSelected>>", on_A_selected)

importance_groups_label = tk.Label(root, text="اهمیت ساختمان", font=custom_font)
importance_groups_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

importance_groups_var = tk.StringVar()
importance_groups_menu = ttk.Combobox(root, textvariable=importance_groups_var, width=20, font=custom_font, justify="right")
importance_groups_menu['values'] = list(importance_groups.keys())
importance_groups_menu.grid(row=3, column=0, padx=10, pady=5, sticky="e")
importance_groups_menu.bind("<<ComboboxSelected>>", on_I_selected)


structure_height_label = tk.Label(root, text="(m) ارتفاع از تراز پایه", font=custom_font, justify="right")
structure_height_label.grid(row=6, column=1, padx=10, pady=5, sticky="e")

structure_height_entry = tk.Entry(root, font=custom_font_Latin, width=10)
structure_height_entry.grid(row=6, column=0, padx=10, pady=5, sticky="e")
structure_height_entry.bind("<Return>", calculate_expression)




soil_type_label = tk.Label(root, text="نوع خاک", font=custom_font, justify="right")
soil_type_label.grid(row=5, column=1, padx=10, pady=5, sticky="e")

soil_type_var = tk.StringVar()
soil_type_menu = ttk.Combobox(root, textvariable=soil_type_var, width=10, font=custom_font_Latin, justify="right")
soil_type_menu['values'] = list(soil_type_data_low_to_medium_A.keys())
soil_type_menu.grid(row=5, column=0, padx=10, pady=5, sticky="e")
soil_type_menu.bind("<<ComboboxSelected>>", on_soil_type_selected)

A_label = tk.Label(root, text="", font=custom_font_Latin)
A_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

I_label = tk.Label(root, text="", font=custom_font_Latin)
I_label.grid(row=2, column=0, padx=100, pady=5, sticky="w")

T0_label = tk.Label(root, text="", font=custom_font_Latin)
T0_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

Ts_label = tk.Label(root, text="", font=custom_font_Latin)
Ts_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

S_label = tk.Label(root, text="", font=custom_font_Latin)
S_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

S0_label = tk.Label(root, text="", font=custom_font_Latin)
S0_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

Ru_label = tk.Label(root, text="", font=custom_font_Latin)
Ru_label.grid(row=3, column=0, padx=100, pady=5, sticky="w")

Ω0_label = tk.Label(root, text="", font=custom_font_Latin)
Ω0_label.grid(row=4, column=0, padx=100, pady=5, sticky="w")

Cd_label = tk.Label(root, text="", font=custom_font_Latin)
Cd_label.grid(row=5, column=0, padx=100, pady=5, sticky="w")

Hm_label = tk.Label(root, text="", font=custom_font_Latin)
Hm_label.grid(row=6, column=0, padx=100, pady=5, sticky="w")

formula_label = tk.Label(root, text="", font=custom_font_Latin, justify="right")
formula_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

N_label = tk.Label(root, text="", font=custom_font_Latin)
N_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

B1_label = tk.Label(root, text="", font=custom_font_Latin)
B1_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")

B_label = tk.Label(root, text="", font=custom_font_Latin)
B_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")

Cmin_label = tk.Label(root, text="", font=custom_font_Latin)
Cmin_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")

k_label = tk.Label(root, text="", font=custom_font_Latin, justify='right')
k_label.grid(row=9, column=0, padx=0, pady=5, sticky="e")
k_button = tk.Button(root, text="", font=custom_font_Latin, command=copy_k_to_clipboard, justify = 'right')
k_button.grid(row=9, column=0, padx=0, pady=5, sticky="e")

C_label = tk.Label(root, text="", font=custom_font_Latin, justify='right')
C_label.grid(row=10, column=0, padx=0, pady=5, sticky="e")
C_button = tk.Button(root, text="", font=custom_font_Latin, command=copy_C_to_clipboard)
C_button.grid(row=10, column=0, padx=0, pady=5, sticky="e")


system_type_label = tk.Label(root, text="نوع سیستم سازه‌ای", font=custom_font, justify='right')
system_type_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")

system_type_var = tk.StringVar()
system_type_menu = ttk.Combobox(root, textvariable=system_type_var, width=31, font=custom_font, justify='right')
system_type_menu['values'] = [
    'سیستم قاب خمشی فولادی',
    'سیستم قاب خمشی فولادی با جداگر میانقابی',
    'سیستم قاب خمشی بتنی',
    'سیستم قاب خمشی بتنی با جداگر میانقابی',
    'سیستم قاب ساختمانی ساده با مهاربند واگرا',
    'سایر سیستم‌های ساختمانی'
]
system_type_menu.grid(row=4, column=0, padx=10, pady=5, sticky="e")

# Add an entry for the analytical period
analytical_T_label = tk.Label(root, text="(s) تحلیلی Tₘ", font=custom_font, justify="right")
analytical_T_label.grid(row=7, column=1, padx=10, pady=5, sticky="e")

analytical_T_entry = tk.Entry(root, font=custom_font_Latin, width=8)
analytical_T_entry.grid(row=7, column=0, padx=10, pady=5, sticky="e")

load_button = tk.Button(root, text="محاسبه", command=on_calculation_clicked, font=custom_font, width=20)
load_button.grid(row=8, column=0, columnspan=3, padx=(0, 50), pady=10, sticky="e")


# # Add labels to display the formula for empirical T and the resultant 1.25 * T
# empirical_T_formula = tk.Label(root, text="", font=custom_font_Latin, justify="left")
# empirical_T_formula.grid(row=13, column=0, columnspan=2, padx=10, pady=5)

# empirical_1_25_T = tk.Label(root, text="", font=custom_font, justify="right")
# empirical_1_25_T.grid(row=14, column=0, columnspan=2, padx=10, pady=5)



message_label = tk.Label(root, text="", font=custom_font, justify="right")
message_label.grid(row=12, column=0, columnspan=3, padx=10, pady=5)

k_copy_message_label = tk.Label(root, text="", font=custom_font, justify="right")
k_copy_message_label.grid(row=9, column=1, columnspan=3, padx=10, pady=5)

C_copy_message_label = tk.Label(root, text="", font=custom_font, justify="right")
C_copy_message_label.grid(row=10, column=1, columnspan=3, padx=10, pady=5)

root.mainloop()


