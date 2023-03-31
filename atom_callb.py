import script as s
import reversed_script as rs

sub_orbital_priority = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d',
                        '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']

sub_orbital_calibration = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6, 2]

atomic_calibre = []
elem_calibre = []
reformatted = []
static_lst = []


def stimulated_calibre(atm):
    print('Electronic configuration : {}'.format(atm))
    j = 0
    for i in range(len(atm)):
        x = ','.join([f'{sub_orbital_priority[j]}{s.sup_script(atm[j])}'])
        j = j + 1  # index increasing
        elem_calibre.append(x)

    last_quantum_no = ((elem_calibre[len(elem_calibre) - 1])[0])
    last_2_quantum_no = ((elem_calibre[len(elem_calibre) - 2])[0])

    for_d_block = ['2p²', '3p²', '4p²', '5p²', '6p²', '7p²', '2p⁵', '3p⁵', '4p⁵', '5p⁵', '6p⁵', '7p⁵',
                   '3d⁴', '4d⁴', '5d⁴', '6d⁴', '3d⁹', '4d⁹', '5d⁹', '6d⁹',
                   '4f⁶', '5f⁶', '4f¹³', '5f¹³']

    # check last two indexes are '4s and 4p or 4d or 5d ..etc'        
    if (elem_calibre[len(elem_calibre) - 1] in for_d_block) and ((elem_calibre[len(elem_calibre) - 2])[1]) == 's' and (
            last_2_quantum_no > last_quantum_no):

        lst_1 = elem_calibre[len(elem_calibre) - 1]
        lst_2 = elem_calibre[len(elem_calibre) - 2]

        # get super script number(s) for resetting
        a1 = (int(rs.reversed_sup_script(lst_1[2:])) + 1)
        a2 = (int(rs.reversed_sup_script(lst_2[2:])) - 1)

        static_lst.append(a2)
        static_lst.append(a1)

        index_num = [lst_2[:2], lst_1[:2]]
        index = 0

        for i in static_lst:
            x_1 = ','.join([f'{index_num[index]}{s.sup_script(i)}'])
            index += 1
            reformatted.append(x_1)

        final_lst = (elem_calibre[:(len(elem_calibre) - 2)]) + reformatted

        c = ' ,'.join([n for n in final_lst])
        print(f'Electronic Calibration : {c}')

    else:
        c = ' ,'.join([n for n in elem_calibre])
        print(f'Electronic Calibration : {c}')

    atomic_calibre.clear()
    elem_calibre.clear()
    reformatted.clear()
    static_lst.clear()


def orbital_filling(nm):
    atom_num = int(nm)
    remainder = 0

    if atom_num <= 2:
        atomic_calibre.append(atom_num)
    else:
        for i in sub_orbital_calibration:
            atom_num = atom_num - i

            if atom_num < 0:
                atomic_calibre.append(remainder)
                break
            else:
                if atom_num == 0:
                    continue
                else:
                    remainder = atom_num
                    atomic_calibre.append(i)

    stimulated_calibre(atomic_calibre)
