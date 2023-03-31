import atom_callb as ac
import json


def main():
    while True:
        atomic_symbol = input('\n>> ').capitalize()

        if atomic_symbol == 'Exit':
            exit()
        elif atomic_symbol == 'Periodic':
            periodic_view()
        else:
            find_key_value(atomic_symbol)


def find_block(json_value, atomic_symbol):
    e_block = ''
    e_group = ''
    try:
        g = (json_value[atomic_symbol]["Group"])

        try:
            e_group = int(g)
        except:
            e_group = g
        finally:

            if e_group == '-':
                e_block = 'f'

            elif e_group < 3:
                e_block = 's'

            elif e_group >= 13:
                e_block = 'p'

            elif 2 < e_group < 13:
                e_block = 'd'

            print(f'Block : {e_block}')

            # set atomic calibration
            get_atomic_num(json_value, atomic_symbol)

    except KeyError:
        print(f"[ Block not detected ] Unknown Element '{atomic_symbol}'")
    except IndexError as ie:
        print(f"[+ find_block ] (May be some list should be clear !); Error : ", ie)
    except Exception as e:
        print('[+ find_block ] Error : ', e)


def get_atomic_num(json_value, atomic_symbol):
    nm = json_value[atomic_symbol]["Atomic Number"]
    ac.orbital_filling(nm)


def find_key_value(atomic_symbol):
    try:
        with open('source_file/per_tbl.json', 'r') as fh:
            json_str = fh.read()
            json_value = json.loads(json_str)
            j_v = json_value[atomic_symbol]

            for key, value in j_v.items():
                print(f'{key} : {value}')
        find_block(json_value, atomic_symbol)

    except KeyError:
        print(f"[ Details not detected ] Unknown Element '{atomic_symbol}'")
    except Exception as e:
        print('[+ find_key_value ]Error : ', e)


periodic_element = ['H', 'He',
                    'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
                    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br',
                    'Kr',
                    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I',
                    'Xe',
                    'Cs', 'Ba',
                    'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                    'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                    'Fr', 'Ra',
                    'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
                    'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo']



def periodic_view():
    
    print('''

        1  2  3  4  5  6  7  8  9  10 11 12 13  14 15  16 17  18
        
        H                                                     He
        Li Be                               B   C  N   O  F   Ne
        Na Mg                               Al  Si P   S  Cl  Ar
        K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga  Ge As  Se Br  Kr
        Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In  Sn Sb  Te I   Xe
        Cs Ba    Hf Ta W  Re Os Ir Pt Au Hg Tl  Pb Bi  Po At  Rn
        Fr Ra    Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Fl Uup Lv Uus Uuo
        
                 La Ce Pr Nd Pm Sm Eu Gd Tb Dy  Ho Er  Tm Yb  Lu
                 Ac Th Pa U  Np Pu Am Cm Bk Cf  Es Fm  Md No  Lr
        
    ''')
    main()

print("""
    [+] Write as "Periodic" for view Periodic Table
    [+] Write the Symbol of the Element which you need to get details
    [+] Write as "Exit" for Exit from the Program    
""")
main()

"""
N.B : 
Not working between Nb - Cd
"""
