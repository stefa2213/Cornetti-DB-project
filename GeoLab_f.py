from tkinter import *
import tkinter.font as font
import GeoLab_b

window = Tk()
window.title("Geo's Lab")
window.geometry('1300x760')
window.configure(bg='#ffdb58')

MY_FONT = 'Arial 10 bold'
FONT_BUTTON = font.Font(size=8)
FONT_LABEL = font.Font(size=8)
FONT_LABEL_PROD = font.Font(size=9)


def get_selected_row_clienti(event):
    try:
        global selected_tuple
        index = lista_clienti.curselection()[0]
        selected_tuple = lista_clienti.get(index)
        sce.delete(0, END)
        sce.insert(END, selected_tuple[1])
    except IndexError:
        pass


def get_selected_row_comenzi(event):
    try:
        global selected_tuple_comanda
        index = lista_comenzi.curselection()[0]
        selected_tuple_comanda = lista_comenzi.get(index)
        lista_q = [sce, sd, q_ciambelle, q_bombe_vuote, q_cbombe_crema, q_bombe_cioc, q_canolli_fr_cr,
                   q_canolli_fr_cioc,
                   q_corn_glassa, q_corn_s_glassa, q_corn_crema, q_corn_cioc, q_corn_marmc, q_corn_marms, q_corn_ciocb,
                   q_fagot_cioc, q_fagot_mele, q_ricotta, q_fagot_bosco, q_campane, q_campane_mar, q_danesi_uva,
                   q_danesi_cioc, q_trecce_granelz, q_trecce_bn, q_stelle_uva, q_radeschi_uva, q_radeschi_cioc,
                   q_radeschi_uva_screma, q_radeschi_cioc_screma, q_veneziane, q_maritozzi, q_canolli_nzcr,
                   q_canolli_nzccioc, q_canolli_crema, q_canolli_cioc, q_canolli_bicc, q_ciambelle_forno,
                   q_inte_ngmiele, q_inte_ngmarsc, q_inte_gelmiele, q_inte_spacmiele, q_inte_sgelatina,
                   q_inte_gelscura, q_inte_sempgel, q_canucci, q_canucci_crema, q_vegani, q_fazzoletti, q_romanisti,
                   q_ciambelle_pi, q_bombe_vuote_pi, q_bombe_crema_pi, q_bombe_cioc_pi, q_fagot_cioc_pi,
                   q_fagot_mele_pi, q_fagot_bosco_pi, q_corn_crema_pi, q_corn_cioc_pi, q_corn_marm_pi, q_corn_semp_pi,
                   q_inte_pi, q_maritozzi_pi]
        ind = 1
        for elem in lista_q:
            elem.delete(0, END)
            elem.insert(END, selected_tuple_comanda[ind])
            ind += 1
    except IndexError:
        pass


# lista clienti
lista_clienti = Listbox(window, width=28, height=28, bd=5, bg='#fafad2')
lista_clienti.grid(row=7, column=0, rowspan=28, columnspan=2, padx=5, pady=2, sticky=W)

sb_clienti = Scrollbar(window, orient=VERTICAL)
sb_clienti.grid(row=7, column=1, rowspan=32, sticky=W)
sb_clienti.configure(command=lista_clienti.yview)

lista_clienti.configure(yscrollcommand=sb_clienti.set)
lista_clienti.bind('<<ListboxSelect>>', get_selected_row_clienti)

# lista comenzi
lista_comenzi = Listbox(window, width=30, height=15, bd=5, bg='#fafad2')
lista_comenzi.grid(row=7, column=2, rowspan=15, columnspan=2, padx=5, pady=2, sticky=N)

lista_comenzi.bind('<<ListboxSelect>>', get_selected_row_comenzi)


def comanda_vizualizare_clienti():
    lista_clienti.delete(0, END)
    for row in GeoLab_b.vizualizeaza_client():
        lista_clienti.insert(END, row)


def comanda_vizualizare_comenzi():
    lista_comenzi.delete(0, END)
    for row in GeoLab_b.vizualizeaza_comanda(selected_client_entry.get()):
        lista_comenzi.insert(END, row)


def comanda_adaugare_clienti():
    GeoLab_b.adauga_client(selected_client_entry.get())
    lista_clienti.delete(0, END)
    # lista_clienti.insert(END, (selected_client_entry.get()))


def comanda_adaugare_comnezi():
    zile = ['Lunedi', 'Martedi', 'Mercoledi', 'Giovedi', 'Venerdi', 'Sabato', 'Domenica', 'LUNEDI', 'MARTEDI',
            'MERCOLEDI', 'GIOVEDI', 'VENERDI', 'SABATO', 'DOMENICA', 'lunedi', 'martedi', 'mercoledi', 'giovedi',
            'venerdi', 'sabato', 'domenica']
    if sd.get() in zile:
        GeoLab_b.adauga_comanda(selected_client_entry.get(), sd.get(), q_ciambelle.get(), q_bombe_vuote.get(),
                                q_cbombe_crema.get(), q_bombe_cioc.get(), q_canolli_fr_cr.get(),
                                q_canolli_fr_cioc.get(),
                                q_corn_glassa.get(), q_corn_s_glassa.get(), q_corn_crema.get(), q_corn_cioc.get(),
                                q_corn_marmc.get(), q_corn_marms.get(), q_corn_ciocb.get(), q_fagot_cioc.get(),
                                q_fagot_mele.get(), q_ricotta.get(), q_fagot_bosco.get(), q_campane.get(),
                                q_campane_mar.get(), q_danesi_uva.get(), q_danesi_cioc.get(),
                                q_trecce_granelz.get(),
                                q_trecce_bn.get(), q_stelle_uva.get(), q_radeschi_uva.get(), q_radeschi_cioc.get(),
                                q_radeschi_uva_screma.get(), q_radeschi_cioc_screma.get(), q_veneziane.get(),
                                q_maritozzi.get(), q_canolli_nzcr.get(), q_canolli_nzccioc.get(),
                                q_canolli_crema.get(),
                                q_canolli_cioc.get(), q_canolli_bicc.get(), q_ciambelle_forno.get(),
                                q_inte_ngmiele.get(),
                                q_inte_ngmarsc.get(), q_inte_gelmiele.get(), q_inte_spacmiele.get(),
                                q_inte_sgelatina.get(), q_inte_gelscura.get(), q_inte_sempgel.get(),
                                q_canucci.get(),
                                q_canucci_crema.get(), q_vegani.get(), q_fazzoletti.get(), q_romanisti.get(),
                                q_ciambelle_pi.get(), q_bombe_vuote_pi.get(), q_bombe_crema_pi.get(),
                                q_bombe_cioc_pi.get(), q_fagot_cioc_pi.get(), q_fagot_mele_pi.get(),
                                q_fagot_bosco_pi.get(), q_corn_crema_pi.get(), q_corn_cioc_pi.get(),
                                q_corn_marm_pi.get(), q_corn_semp_pi.get(), q_inte_pi.get(), q_maritozzi_pi.get())
        lista_comenzi.delete(0, END)
        # lista_comenzi.insert(END, (selected_client_entry.get(), sd.get(), q_ciambelle.get(), q_bombe_vuote.get(),
        #                            q_cbombe_crema.get(), q_bombe_cioc.get(), q_canolli_fr_cr.get(),
        #                            q_canolli_fr_cioc.get(),
        #                            q_corn_glassa.get(), q_corn_s_glassa.get(), q_corn_crema.get(),
        #                            q_corn_cioc.get(),
        #                            q_corn_marmc.get(), q_corn_marms.get(), q_corn_ciocb.get(), q_fagot_cioc.get(),
        #                            q_fagot_mele.get(), q_ricotta.get(), q_fagot_bosco.get(), q_campane.get(),
        #                            q_campane_mar.get(), q_danesi_uva.get(), q_danesi_cioc.get(),
        #                            q_trecce_granelz.get(),
        #                            q_trecce_bn.get(), q_stelle_uva.get(), q_radeschi_uva.get(),
        #                            q_radeschi_cioc.get(),
        #                            q_radeschi_uva_screma.get(), q_radeschi_cioc_screma.get(), q_veneziane.get(),
        #                            q_maritozzi.get(), q_canolli_nzcr.get(), q_canolli_nzccioc.get(),
        #                            q_canolli_crema.get(),
        #                            q_canolli_cioc.get(), q_canolli_bicc.get(), q_ciambelle_forno.get(),
        #                            q_inte_ngmiele.get(),
        #                            q_inte_ngmarsc.get(), q_inte_gelmiele.get(), q_inte_spacmiele.get(),
        #                            q_inte_sgelatina.get(), q_inte_gelscura.get(), q_inte_sempgel.get(),
        #                            q_canucci.get(),
        #                            q_canucci_crema.get(), q_vegani.get(), q_fazzoletti.get(), q_romanisti.get(),
        #                            q_ciambelle_pi.get(), q_bombe_vuote_pi.get(), q_bombe_crema_pi.get(),
        #                            q_bombe_cioc_pi.get(), q_fagot_cioc_pi.get(), q_fagot_mele_pi.get(),
        #                            q_fagot_bosco_pi.get(), q_corn_crema_pi.get(), q_corn_cioc_pi.get(),
        #                            q_corn_marm_pi.get(), q_corn_semp_pi.get(), q_inte_pi.get(),
        #                            q_maritozzi_pi.get()))
    else:
        notificare = Tk()
        notificare.title('Avvertimento')
        notificare.geometry('400x70')
        notificare.configure(bg='#ffdb58')
        l_notificare = Label(notificare, text='Hai dimenticato di inserire un giorno, Riprova!', font=FONT_LABEL,
                             anchor=CENTER, bg='#ffdb58')
        l_notificare.grid(row=0, column=2)
        bnotificare = Button(notificare, text='OK', font=FONT_LABEL, command=notificare.destroy)
        bnotificare.grid(row=1, column=2)
        notificare.mainloop()


def comanda_modificare_clienti():
    GeoLab_b.modifica_client(selected_tuple[0])


def comanda_modificare_comenzi():
    GeoLab_b.modifica_comanda(selected_tuple_comanda[0], selected_client_entry.get(), sd.get(), q_ciambelle.get(),
                              q_bombe_vuote.get(),
                              q_cbombe_crema.get(), q_bombe_cioc.get(), q_canolli_fr_cr.get(), q_canolli_fr_cioc.get(),
                              q_corn_glassa.get(), q_corn_s_glassa.get(), q_corn_crema.get(), q_corn_cioc.get(),
                              q_corn_marmc.get(), q_corn_marms.get(), q_corn_ciocb.get(), q_fagot_cioc.get(),
                              q_fagot_mele.get(), q_ricotta.get(), q_fagot_bosco.get(), q_campane.get(),
                              q_campane_mar.get(), q_danesi_uva.get(), q_danesi_cioc.get(), q_trecce_granelz.get(),
                              q_trecce_bn.get(), q_stelle_uva.get(), q_radeschi_uva.get(), q_radeschi_cioc.get(),
                              q_radeschi_uva_screma.get(), q_radeschi_cioc_screma.get(), q_veneziane.get(),
                              q_maritozzi.get(), q_canolli_nzcr.get(), q_canolli_nzccioc.get(), q_canolli_crema.get(),
                              q_canolli_cioc.get(), q_canolli_bicc.get(), q_ciambelle_forno.get(),
                              q_inte_ngmiele.get(),
                              q_inte_ngmarsc.get(), q_inte_gelmiele.get(), q_inte_spacmiele.get(),
                              q_inte_sgelatina.get(), q_inte_gelscura.get(), q_inte_sempgel.get(), q_canucci.get(),
                              q_canucci_crema.get(), q_vegani.get(), q_fazzoletti.get(), q_romanisti.get(),
                              q_ciambelle_pi.get(), q_bombe_vuote_pi.get(), q_bombe_crema_pi.get(),
                              q_bombe_cioc_pi.get(), q_fagot_cioc_pi.get(), q_fagot_mele_pi.get(),
                              q_fagot_bosco_pi.get(), q_corn_crema_pi.get(), q_corn_cioc_pi.get(),
                              q_corn_marm_pi.get(), q_corn_semp_pi.get(), q_inte_pi.get(), q_maritozzi_pi.get())

    notificare_modif = Tk()
    notificare_modif.title("Notifica")
    notificare_modif.geometry('240x80')
    notificare_modif.configure(bg='#ffdb58')
    lavert = Label(notificare_modif, text="L'ordine e stato modificato", font=FONT_LABEL, bg='#ffdb58', anchor=CENTER)
    lavert.grid(row=0, column=2, columnspan=2)
    bno = Button(notificare_modif, text='Ok', font=FONT_LABEL, command=notificare_modif.destroy)
    bno.grid(row=1, column=2)


def comanda_stergere_clienti():
    def sterge():
        GeoLab_b.sterge_client(selected_tuple[0])
        window_notificare_stergere = Tk()
        lnotif = Label(window_notificare_stergere, text='I dati del cliente sono stati cancellati!', font=FONT_LABEL,
                       anchor=CENTER)
        lnotif.grid(row=0, column=2)
        f1 = window_stergere.destroy
        f2 = window_notificare_stergere.destroy
        bnotif = Button(window_notificare_stergere, text='OK', font=FONT_LABEL, command=lambda: [f1(), f2()])
        bnotif.grid(row=1, column=2)
        window_notificare_stergere.title('Confirmare')
        window_notificare_stergere.geometry('330x80')
        window_notificare_stergere.mainloop()
        window_notificare_stergere.destroy()

    window_stergere = Tk()
    lavert = Label(window_stergere, text='Sei sicuro di voler eliminare questo client?', font=FONT_LABEL, anchor=CENTER)
    lavert.grid(row=0, column=2, columnspan=2)
    byes = Button(window_stergere, text='Si', font=FONT_LABEL, anchor=CENTER, command=sterge)
    byes.grid(row=2, column=2)
    bno = Button(window_stergere, text='No', font=FONT_LABEL, anchor=CENTER, command=window_stergere.destroy)
    bno.grid(row=2, column=3)
    window_stergere.title("Avvertimento")
    window_stergere.geometry('380x80')
    window_stergere.mainloop()


def comanda_stergere_comenzi():
    def sterge():
        GeoLab_b.sterge_comanda(selected_tuple_comanda[0])
        window_notificare_stergere = Tk()
        lnotif = Label(window_notificare_stergere, text="L'ordine è stato cancellato!", font=FONT_LABEL,
                       anchor=CENTER)
        lnotif.grid(row=0, column=2)
        f1 = window_stergere.destroy
        f2 = window_notificare_stergere.destroy
        bnotif = Button(window_notificare_stergere, text='OK', font=FONT_LABEL, command=lambda: [f1(), f2()])
        bnotif.grid(row=1, column=2)
        window_notificare_stergere.title('Confirmare')
        window_notificare_stergere.geometry('270x80')
        window_notificare_stergere.mainloop()
        window_notificare_stergere.destroy()

    window_stergere = Tk()
    lavert = Label(window_stergere, text='Sei sicuro di voler eliminare questo ordine?', font=FONT_LABEL, anchor=CENTER)
    lavert.grid(row=0, column=2, columnspan=2)
    byes = Button(window_stergere, text='Si', font=FONT_LABEL, anchor=CENTER, command=sterge)
    byes.grid(row=2, column=2)
    bno = Button(window_stergere, text='No', font=FONT_LABEL, anchor=CENTER, command=window_stergere.destroy)
    bno.grid(row=2, column=3)
    window_stergere.title("Avvertimento")
    window_stergere.geometry('380x80')
    window_stergere.mainloop()


def comanda_elimina_campuri():
    lista_campuri = [sd, sce, q_ciambelle, q_bombe_vuote, q_cbombe_crema, q_bombe_cioc,
                     q_canolli_fr_cr, q_canolli_fr_cioc,
                     q_corn_glassa, q_corn_s_glassa, q_corn_crema, q_corn_cioc, q_corn_marmc, q_corn_marms,
                     q_corn_ciocb,
                     q_fagot_cioc, q_fagot_mele, q_ricotta, q_fagot_bosco, q_campane, q_campane_mar, q_danesi_uva,
                     q_danesi_cioc, q_trecce_granelz, q_trecce_bn, q_stelle_uva, q_radeschi_uva, q_radeschi_cioc,
                     q_radeschi_uva_screma, q_radeschi_cioc_screma, q_veneziane, q_maritozzi, q_canolli_nzcr,
                     q_canolli_nzccioc, q_canolli_crema, q_canolli_cioc, q_canolli_bicc, q_ciambelle_forno,
                     q_inte_ngmiele, q_inte_ngmarsc, q_inte_gelmiele, q_inte_spacmiele, q_inte_sgelatina,
                     q_inte_gelscura, q_inte_sempgel, q_canucci, q_canucci_crema, q_vegani, q_fazzoletti, q_romanisti,
                     q_ciambelle_pi, q_bombe_vuote_pi, q_bombe_crema_pi, q_bombe_cioc_pi, q_fagot_cioc_pi,
                     q_fagot_mele_pi, q_fagot_bosco_pi, q_corn_crema_pi, q_corn_cioc_pi, q_corn_marm_pi, q_corn_semp_pi,
                     q_inte_pi, q_maritozzi_pi]
    for elem in lista_campuri:
        elem.delete(0, END)


# def calculeaza_fri():
#     calculated = GeoLab_b.calc_totale_fritti(sd.get())
#     calc_fr = Label(window, text=calculated, font=MY_FONT, bg='#ffdb58', fg='dark blue')
#     calc_fr.grid(row=24, column=9, sticky=E)
#     calc_fr['font'] = FONT_LABEL
#
#
# def calculeaza_fri_pi():
#     calculated = GeoLab_b.calc_totale_fritti_picc(sd.get())
#     calc_fr_pi = Label(window, text=calculated, font=MY_FONT, bg='#ffdb58', fg='dark blue')
#     calc_fr_pi.grid(row=26, column=9, sticky=E)
#     calc_fr_pi['font'] = FONT_LABEL
#
#
# def calculeaza_pi():
#     calculated = GeoLab_b.calc_totale_picc(sd.get())
#     calc_pi = Label(window, text=calculated, font=MY_FONT, bg='#ffdb58', fg='dark blue')
#     calc_pi.grid(row=25, column=9, sticky=E)
#     calc_pi['font'] = FONT_LABEL
#
#
# def calculeaza_grandi():
#     calculated = GeoLab_b.calc_totale_grandi(sd.get())
#     calc_pi = Label(window, text=calculated, font=MY_FONT, bg='#ffdb58', fg='dark blue')
#     calc_pi.grid(row=23, column=9, sticky=E)
#     calc_pi['font'] = FONT_LABEL


FONT_LABEL_CALC = font.Font(size=2)


def calcul():
    calculeaza = Tk()
    calculeaza.title('Calcolare')
    calculeaza.geometry('670x500')
    calculeaza.configure(bg='#ffdb58')
    l_totale1 = ['INTEGRALI-', 'INTEGRALI PICC.-', 'VENEZIANE-', 'MARITOZZI-', 'TRECCE-', 'CANNUCCI-',
                 'CIAMBELLE FORNO-',
                 'FAZOLETTI-', 'RICOTTA-', 'CANNOLI-', 'STELLE-', 'ROMANISTI-', 'FAGOTTINI CIOC.-', 'FAGOTTINI MELE-',
                 'FAGOTTINI BOSCO-', 'FAGOTTINI PICC. CIOC.-']
    l_totale2 = ['FAGOTTINI PICC. MELLE-', 'FAGOTTINI PICC. BOSCO-', 'RADESCHI UVA-', 'DANESI UVA-',
                 'RADESCHI CIOC.-', 'DANESI CIOC.-', 'CAMPANE-', 'CORNETTI PICC.-', 'CORNETTI-', 'BOMBE-',
                 'BOMBE PICC.-',
                 'CIAMBELLE PICC.-', 'CANNOLI FRITTI-', 'CIAMBELLE-']
    row_tot1 = 1
    for t in l_totale1:
        lab_totale = Label(calculeaza, text=t, bg='#ffdb58', fg='dark blue', font=FONT_LABEL_CALC)
        lab_totale.grid(row=row_tot1, column=0, sticky=E)
        row_tot1 += 1
    row_tot2 = 1
    for t in l_totale2:
        lab_totale = Label(calculeaza, text=t, bg='#ffdb58', fg='dark blue', font=FONT_LABEL_CALC)
        lab_totale.grid(row=row_tot2, column=2, sticky=E)
        row_tot2 += 1

    calculated_cornetti = GeoLab_b.calc_totale_cornetti(sd.get())
    calc_fr = Label(calculeaza, text=calculated_cornetti, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=9, column=3, sticky=W)

    calculated_bombe = GeoLab_b.calc_totale_bombe(sd.get())
    calc_fr = Label(calculeaza, text=calculated_bombe, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=10, column=3, sticky=W)

    calculated_cann_fri = GeoLab_b.calc_totale_cann_fri(sd.get())
    calc_fr = Label(calculeaza, text=calculated_cann_fri, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=13, column=3, sticky=W)

    calculated_dan_uv = GeoLab_b.calc_totale_dan_uv(sd.get())
    calc_fr = Label(calculeaza, text=calculated_dan_uv, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=4, column=3, sticky=W)

    calculated_tre = GeoLab_b.calc_totale_tre(sd.get())
    calc_fr = Label(calculeaza, text=calculated_tre, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=5, column=1, sticky=W)

    calculated_cano = GeoLab_b.calc_totale_cano(sd.get())
    calc_fr = Label(calculeaza, text=calculated_cano, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=10, column=1, sticky=W)

    calculated_integr = GeoLab_b.calc_totale_integr(sd.get())
    calc_fr = Label(calculeaza, text=calculated_integr, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=1, column=1, sticky=W)

    calculated_cann = GeoLab_b.calc_totale_cann(sd.get())
    calc_fr = Label(calculeaza, text=calculated_cann, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=6, column=1, sticky=W)

    calculated_corn_picc = GeoLab_b.calc_totale_corn_picc(sd.get())
    calc_fr = Label(calculeaza, text=calculated_corn_picc, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=8, column=3, sticky=W)

    calculated_bomb_picc = GeoLab_b.calc_totale_bomb_picc(sd.get())
    calc_fr = Label(calculeaza, text=calculated_bomb_picc, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=11, column=3, sticky=W)

    calculated_ciam = GeoLab_b.calc_totale_ciam(sd.get())
    calc_fr = Label(calculeaza, text=calculated_ciam, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=14, column=3, sticky=W)

    calculated_fagci = GeoLab_b.calc_totale_fagci(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagci, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=13, column=1, sticky=W)

    calculated_fagbo = GeoLab_b.calc_totale_fagbo(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagbo, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=15, column=1, sticky=W)

    calculated_fagme = GeoLab_b.calc_totale_fagme(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagme, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=14, column=1, sticky=W)

    calculated_campa = GeoLab_b.calc_totale_campa(sd.get())
    calc_fr = Label(calculeaza, text=calculated_campa, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=7, column=3, sticky=W)

    calculated_danci = GeoLab_b.calc_totale_danci(sd.get())
    calc_fr = Label(calculeaza, text=calculated_danci, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=6, column=3, sticky=W)

    calculated_steuv = GeoLab_b.calc_totale_steuv(sd.get())
    calc_fr = Label(calculeaza, text=calculated_steuv, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=11, column=1, sticky=W)

    calculated_rade = GeoLab_b.calc_totale_rade(sd.get())
    calc_fr = Label(calculeaza, text=calculated_rade, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=3, column=3, sticky=W)

    calculated_danci = GeoLab_b.calc_totale_danci(sd.get())
    calc_fr = Label(calculeaza, text=calculated_danci, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=5, column=3, sticky=W)

    calculated_vene = GeoLab_b.calc_totale_vene(sd.get())
    calc_fr = Label(calculeaza, text=calculated_vene, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=3, column=1, sticky=W)

    calculated_mari = GeoLab_b.calc_totale_mari(sd.get())
    calc_fr = Label(calculeaza, text=calculated_mari, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=4, column=1, sticky=W)

    calculated_ciamfo = GeoLab_b.calc_totale_ciamfo(sd.get())
    calc_fr = Label(calculeaza, text=calculated_ciamfo, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=7, column=1, sticky=W)

    calculated_fazz = GeoLab_b.calc_totale_fazz(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fazz, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=8, column=1, sticky=W)

    calculated_roma = GeoLab_b.calc_totale_roma(sd.get())
    calc_fr = Label(calculeaza, text=calculated_roma, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=12, column=1, sticky=W)

    calculated_ciampi = GeoLab_b.calc_totale_ciampi(sd.get())
    calc_fr = Label(calculeaza, text=calculated_ciampi, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=12, column=3, sticky=W)

    calculated_fagpi = GeoLab_b.calc_totale_fagpi(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagpi, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=16, column=1, sticky=W)

    calculated_fagmepi = GeoLab_b.calc_totale_fagmepi(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagmepi, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=1, column=3, sticky=W)

    calculated_fagbospi = GeoLab_b.calc_totale_fagbospi(sd.get())
    calc_fr = Label(calculeaza, text=calculated_fagbospi, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=2, column=3, sticky=W)

    calculated_rico = GeoLab_b.calc_totale_rico(sd.get())
    calc_fr = Label(calculeaza, text=calculated_rico, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=9, column=1, sticky=W)

    calculated_intpi = GeoLab_b.calc_totale_intpi(sd.get())
    calc_fr = Label(calculeaza, text=calculated_intpi, bg='#ffdb58', fg='green', font=FONT_LABEL_CALC)
    calc_fr.grid(row=2, column=1, sticky=W)


calc = Button(window, text='Calcola Totale', font=MY_FONT, bg='light green', fg='black', activebackground='#ffdb58',
              width=15, height=1, bd=3, command=calcul)
calc.grid(row=0, column=2)

# day_selected
selected_day_lab = Label(window, text='GIORNO:', bg='#ffdb58', fg='dark blue')
selected_day_lab.grid(row=0, column=0, sticky=E)
selected_day_lab['font'] = FONT_LABEL_PROD

selected_day = StringVar()
sd = Entry(window, textvariable=selected_day, width=11, font=FONT_LABEL, bg='#fafad2', fg='green', bd=3)
sd.grid(row=0, column=1, sticky=W, padx=5, pady=2)

# buttons
show_but_client = Button(window, text='MOSTRA CLIENTI', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                         activebackground='#ffdb58', width=20, command=comanda_vizualizare_clienti, bd=3)
show_but_client.grid(row=6, column=0, sticky=W, padx=5, pady=2)

add_but_client = Button(window, text='INSERIRE CLIENTE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                        activebackground='#ffdb58', width=20, command=comanda_adaugare_clienti, bd=3)
add_but_client.grid(row=5, column=0, padx=5, pady=2)

modify_but_client = Button(window, text='MODIFICARE CLIENTE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                           activebackground='#ffdb58', width=20, command=comanda_modificare_clienti, bd=3)
modify_but_client.grid(row=4, column=0, padx=5, pady=2)

delete_but_client = Button(window, text='ELIMINARE CLIENTE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                           activebackground='#ff4040', width=20, command=comanda_stergere_clienti, bd=3)
delete_but_client.grid(row=3, column=0, padx=5, pady=2)

show_but_order = Button(window, text='MOSTRA GLI ORDINI', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                        activebackground='#ffdb58', width=20, bd=3, command=comanda_vizualizare_comenzi)
show_but_order.grid(row=6, column=2, padx=5, pady=2)

add_but_order = Button(window, text='INSERIRE ORDINE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                       activebackground='#ffdb58', width=20, bd=3, command=comanda_adaugare_comnezi)
add_but_order.grid(row=5, column=2, padx=5, pady=2)

modify_but_order = Button(window, text='MODIFICARE ORDINE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                          activebackground='#ffdb58', width=20, bd=3, command=comanda_modificare_comenzi)
modify_but_order.grid(row=4, column=2, padx=5, pady=2)

delete_but_order = Button(window, text='ELIMINARE ORDINE', font=MY_FONT, bg='#f5fffa', fg='dark blue',
                          activebackground='#ff4040', width=20, bd=3, command=comanda_stergere_comenzi)
delete_but_order.grid(row=3, column=2, padx=5, pady=2)

clear_but = Button(window, text='Rimuovere Tutti Campi', font=MY_FONT, bg='#f5fffa', fg='black',
                   activebackground='#ffdb58', width=18, bd=2, command=comanda_elimina_campuri)
clear_but.grid(row=1, column=2)

# clienti
selected_client = Label(window, text='CLIENTE:', bg='#ffdb58', fg='dark blue')
selected_client.grid(row=1, column=0, sticky=E)
selected_client['font'] = FONT_LABEL_PROD

selected_client_entry = StringVar()
sce = Entry(window, textvariable=selected_client_entry, width=18, font=FONT_LABEL, bg='#fafad2',
            fg='green', bd=3)
sce.grid(row=1, column=1, sticky=W, padx=5, pady=1)

# produse
produse_lab = Label(window, text='Prodotti', bg='#ffdb58', fg='dark blue')
produse_lab.grid(row=1, column=4, sticky=E)
produse_lab['font'] = FONT_LABEL_PROD

produse_lab = Label(window, text='Prodotti', bg='#ffdb58', fg='dark blue')
produse_lab.grid(row=1, column=6, sticky=E)
produse_lab['font'] = FONT_LABEL_PROD

produse_lab = Label(window, text='Prodotti piccoli', bg='#ffdb58', fg='dark blue')
produse_lab.grid(row=1, column=8, sticky=E)
produse_lab['font'] = FONT_LABEL_PROD


def add_product(text, row, column=4, font=MY_FONT, bg='#ffdb58', fg='dark blue'):
    prod = Label(window, text=text, font=font, bg=bg, fg=fg)
    prod.grid(row=row, column=column, sticky=E, pady=2)
    prod['font'] = FONT_LABEL_PROD


add_product('CIAMBELLE', 2)
add_product('BOMBE VUOTE', 3)
add_product('BOMBE CREMA', 4)
add_product('BOMBE CIOC.', 5)
add_product('CANOLLI FRITTI CR.', 6)
add_product('CANOLLI FRITTI CIOC.', 7)
add_product('CORNETTI GLASSA', 8)
add_product('CORNETTI SENZA GLASSA', 9)
add_product('CORNETTI CREMA', 10)
add_product('CORNETTI CIOC.', 11)
add_product('CORNETTI MARM. CH', 12)
add_product('CORNETTI MARM. SC.', 13)
add_product('CORNETTI CIOC. BIANCO', 14)
add_product('FAGOTTINI CIOC.', 15)
add_product('FAGOTTINI MELE', 16)
add_product('RICOTTA', 17)
add_product('FAGOTTINI BOSCO', 18)
add_product('CAMPANE', 19)
add_product('CAMPANA MARMELADA', 20)
add_product('DANESI UVA', 21)
add_product('DANESI CIOC.', 22)
add_product('TRECCE GRANELLA ZUCCH.', 23)
add_product('TRECCE B/N', 24)
add_product('STELLE UVA', 25)



def add_product(text, row, column=6, font=MY_FONT, bg='#ffdb58', fg='dark blue'):
    prod = Label(window, text=text, font=font, bg=bg, fg=fg)
    prod.grid(row=row, column=column, sticky=E, pady=2)
    prod['font'] = FONT_LABEL_PROD


add_product('RADESCHI CIOC.', 2)
add_product('RADESCHI UVA NO CREMA', 3)
add_product('RADESCHI CIOC NO CREMA', 4)
add_product('VENEZIANE', 5)
add_product('MARITOZZI', 6)
add_product('CANOLLI NZ CREMA', 7)
add_product('CANOLLI NZ CIOC.', 8)
add_product('CANOLLI CREMA', 9)
add_product('CANOLLI CIOC.', 10)
add_product('CANOLLI BICCOLORI', 11)
add_product('CIAMBELLE FORNO', 12)
add_product('INTEGRALI NG. MIELE', 13)
add_product('INTEGRALI NG. MAR. SC.', 14)
add_product('INTEGRALI GEL. MIELE', 15)
add_product('INTEGRALI SPAC. MIELE', 16)
add_product('INTEGRALI SENZA GELATINA', 17)
add_product('INTEGRALI GEL. SCURA', 18)
add_product('INTEGRALI SEMPLICI GEL.', 19)
add_product('CANUCCI', 20)
add_product('CANNUCCI CREMA', 21)
add_product('VEGANI', 22)
add_product('FAZZOLETTI', 23)
add_product('ROMANISTI', 24)
add_product('RADESCHI UVA', 25)


def add_product(text, row, column=8, font=MY_FONT, bg='#ffdb58', fg='dark blue'):
    prod = Label(window, text=text, font=font, bg=bg, fg=fg)
    prod.grid(row=row, column=column, sticky=E, pady=2)
    prod['font'] = FONT_LABEL_PROD


add_product('CIAMBELLE PICC.', 2)
add_product('BOMBE VUOTE PICC.', 3)
add_product('BOMBE CREMA PICC.', 4)
add_product('BOMBE CIOC. PICC.', 5)
add_product('FAGOTTINI PICC.', 6)
add_product('FAGOTTINI MELE PICC.', 7)
add_product('FAGOTTINI BOSCO PICC.', 8)
add_product('CORNETT CREMA PICC.', 9)
add_product('CORNETTI CIOC. PICC.', 10)
add_product('CORNETTI MARM. PICC.', 11)
add_product('CORNETTI SEMPLICI PICC.', 12)
add_product('INTEGRALI PICC.', 13)
add_product('MARITOZZI PICC.', 14)

# cantitate_produse - randul 1
cantitate_lab = Label(window, text='/ Quantità', font=MY_FONT, bg='#ffdb58', fg='dark blue')
cantitate_lab.grid(row=1, column=5, sticky=W)
cantitate_lab['font'] = FONT_LABEL_PROD

qval_ciambelle = StringVar()
q_ciambelle = Entry(window, textvariable=qval_ciambelle, width=6, font=FONT_LABEL, bg='#fafad2', fg='green', bd=3)
q_ciambelle.grid(row=2, column=5)

qval_bombe_vuote = StringVar()
q_bombe_vuote = Entry(window, textvariable=qval_bombe_vuote, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                      bd=3)
q_bombe_vuote.grid(row=3, column=5)

qval_bombe_crema = StringVar()
q_cbombe_crema = Entry(window, textvariable=qval_bombe_crema, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_cbombe_crema.grid(row=4, column=5)

qval_bombe_cioc = StringVar()
q_bombe_cioc = Entry(window, textvariable=qval_bombe_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_bombe_cioc.grid(row=5, column=5)

qval_canolli_fr_cr = StringVar()
q_canolli_fr_cr = Entry(window, textvariable=qval_canolli_fr_cr, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_canolli_fr_cr.grid(row=6, column=5)

qval_canolli_fr_cioc = StringVar()
q_canolli_fr_cioc = Entry(window, textvariable=qval_canolli_fr_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                          bd=3)
q_canolli_fr_cioc.grid(row=7, column=5)

qval_corn_glassa = StringVar()
q_corn_glassa = Entry(window, textvariable=qval_corn_glassa, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                      bd=3)
q_corn_glassa.grid(row=8, column=5)

qval_corn_s_glassa = StringVar()
q_corn_s_glassa = Entry(window, textvariable=qval_corn_s_glassa, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_corn_s_glassa.grid(row=9, column=5)

qval_corn_crema = StringVar()
q_corn_crema = Entry(window, textvariable=qval_corn_crema, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_corn_crema.grid(row=10, column=5)

qval_corn_cioc = StringVar()
q_corn_cioc = Entry(window, textvariable=qval_corn_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                    bd=3)
q_corn_cioc.grid(row=11, column=5)

qval_corn_marmc = StringVar()
q_corn_marmc = Entry(window, textvariable=qval_corn_marmc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_corn_marmc.grid(row=12, column=5)

qval_corn_marms = StringVar()
q_corn_marms = Entry(window, textvariable=qval_corn_marms, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_corn_marms.grid(row=13, column=5)

qval_corn_ciocb = StringVar()
q_corn_ciocb = Entry(window, textvariable=qval_corn_ciocb, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_corn_ciocb.grid(row=14, column=5)

qval_fagot_cioc = StringVar()
q_fagot_cioc = Entry(window, textvariable=qval_fagot_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_fagot_cioc.grid(row=15, column=5)

qval_fagot_mele = StringVar()
q_fagot_mele = Entry(window, textvariable=qval_fagot_mele, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_fagot_mele.grid(row=16, column=5)

qval_ricotta = StringVar()
q_ricotta = Entry(window, textvariable=qval_ricotta, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                  bd=3)
q_ricotta.grid(row=17, column=5)

qval_fagot_bosco = StringVar()
q_fagot_bosco = Entry(window, textvariable=qval_fagot_bosco, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                      bd=3)
q_fagot_bosco.grid(row=18, column=5)

qval_campane = StringVar()
q_campane = Entry(window, textvariable=qval_campane, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                  bd=3)
q_campane.grid(row=19, column=5)

qval_campane_mar = StringVar()
q_campane_mar = Entry(window, textvariable=qval_campane_mar, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                      bd=3)
q_campane_mar.grid(row=20, column=5)

qval_danesi_uva = StringVar()
q_danesi_uva = Entry(window, textvariable=qval_danesi_uva, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_danesi_uva.grid(row=21, column=5)

qval_danesi_cioc = StringVar()
q_danesi_cioc = Entry(window, textvariable=qval_danesi_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                      bd=3)
q_danesi_cioc.grid(row=22, column=5)

qval_trecce_granelz = StringVar()
q_trecce_granelz = Entry(window, textvariable=qval_trecce_granelz, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_trecce_granelz.grid(row=23, column=5)

qval_trecce_bn = StringVar()
q_trecce_bn = Entry(window, textvariable=qval_trecce_bn, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                    bd=3)
q_trecce_bn.grid(row=24, column=5)

qval_stelle_uva = StringVar()
q_stelle_uva = Entry(window, textvariable=qval_stelle_uva, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_stelle_uva.grid(row=25, column=5)



# cantitate_produse - randul 2
cantitate_lab = Label(window, text='/ Quantità', font=MY_FONT, bg='#ffdb58', fg='dark blue')
cantitate_lab.grid(row=1, column=7, sticky=W)
cantitate_lab['font'] = FONT_LABEL_PROD

qval_radeschi_cioc = StringVar()
q_radeschi_cioc = Entry(window, textvariable=qval_radeschi_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_radeschi_cioc.grid(row=2, column=7)

qval_radeschi_uva_screma = StringVar()
q_radeschi_uva_screma = Entry(window, textvariable=qval_radeschi_uva_screma, width=6, font=FONT_LABEL, bg='#fafad2',
                              fg='green',
                              bd=3)
q_radeschi_uva_screma.grid(row=3, column=7)

qval_radeschi_cioc_screma = StringVar()
q_radeschi_cioc_screma = Entry(window, textvariable=qval_radeschi_cioc_screma, width=6, font=FONT_LABEL, bg='#fafad2',
                               fg='green',
                               bd=3)
q_radeschi_cioc_screma.grid(row=4, column=7)

qval_veneziane = StringVar()
q_veneziane = Entry(window, textvariable=qval_veneziane, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                    bd=3)
q_veneziane.grid(row=5, column=7)

qval_maritozzi = StringVar()
q_maritozzi = Entry(window, textvariable=qval_maritozzi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                    bd=3)
q_maritozzi.grid(row=6, column=7)

qval_canolli_nzcr = StringVar()
q_canolli_nzcr = Entry(window, textvariable=qval_canolli_nzcr, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_canolli_nzcr.grid(row=7, column=7)

qval_canolli_nzcioc = StringVar()
q_canolli_nzccioc = Entry(window, textvariable=qval_canolli_nzcioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                          bd=3)
q_canolli_nzccioc.grid(row=8, column=7)

qval_canolli_crema = StringVar()
q_canolli_crema = Entry(window, textvariable=qval_canolli_crema, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_canolli_crema.grid(row=9, column=7)

qval_canolli_cioc = StringVar()
q_canolli_cioc = Entry(window, textvariable=qval_canolli_cioc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_canolli_cioc.grid(row=10, column=7)

qval_canolli_bicc = StringVar()
q_canolli_bicc = Entry(window, textvariable=qval_canolli_bicc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_canolli_bicc.grid(row=11, column=7)

qval_ciambelle_forno = StringVar()
q_ciambelle_forno = Entry(window, textvariable=qval_ciambelle_forno, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                          bd=3)
q_ciambelle_forno.grid(row=12, column=7)

qval_inte_ngmiele = StringVar()
q_inte_ngmiele = Entry(window, textvariable=qval_inte_ngmiele, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_inte_ngmiele.grid(row=13, column=7)

qval_inte_ngmarsc = StringVar()
q_inte_ngmarsc = Entry(window, textvariable=qval_inte_ngmarsc, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_inte_ngmarsc.grid(row=14, column=7)

qval_inte_gelmiele = StringVar()
q_inte_gelmiele = Entry(window, textvariable=qval_inte_gelmiele, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_inte_gelmiele.grid(row=15, column=7)

qval_inte_spacmiele = StringVar()
q_inte_spacmiele = Entry(window, textvariable=qval_inte_spacmiele, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_inte_spacmiele.grid(row=16, column=7)

qval_inte_sgelatina = StringVar()
q_inte_sgelatina = Entry(window, textvariable=qval_inte_sgelatina, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_inte_sgelatina.grid(row=17, column=7)

qval_inte_gelscura = StringVar()
q_inte_gelscura = Entry(window, textvariable=qval_inte_gelscura, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_inte_gelscura.grid(row=18, column=7)

qval_inte_sempgel = StringVar()
q_inte_sempgel = Entry(window, textvariable=qval_inte_sempgel, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_inte_sempgel.grid(row=19, column=7)

qval_canucci = StringVar()
q_canucci = Entry(window, textvariable=qval_canucci, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                  bd=3)
q_canucci.grid(row=20, column=7)

qval_canucci_crema = StringVar()
q_canucci_crema = Entry(window, textvariable=qval_canucci_crema, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_canucci_crema.grid(row=21, column=7)

qval_vegani = StringVar()
q_vegani = Entry(window, textvariable=qval_vegani, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                 bd=3)
q_vegani.grid(row=22, column=7)

qval_fazzoletti = StringVar()
q_fazzoletti = Entry(window, textvariable=qval_fazzoletti, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                     bd=3)
q_fazzoletti.grid(row=23, column=7)

qval_romanisti = StringVar()
q_romanisti = Entry(window, textvariable=qval_romanisti, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                    bd=3)
q_romanisti.grid(row=24, column=7)

qval_radeschi_uva = StringVar()
q_radeschi_uva = Entry(window, textvariable=qval_radeschi_uva, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_radeschi_uva.grid(row=25, column=7)

# cantitate_produse - randul 3
cantitate_lab = Label(window, text='/ Quantità', font=MY_FONT, bg='#ffdb58', fg='dark blue')
cantitate_lab.grid(row=1, column=9, sticky=W)
cantitate_lab['font'] = FONT_LABEL_PROD

qval_ciambelle_pi = StringVar()
q_ciambelle_pi = Entry(window, textvariable=qval_ciambelle_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_ciambelle_pi.grid(row=2, column=9)

qval_bombe_vuote_pi = StringVar()
q_bombe_vuote_pi = Entry(window, textvariable=qval_bombe_vuote_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_bombe_vuote_pi.grid(row=3, column=9)

qval_bombe_crema_pi = StringVar()
q_bombe_crema_pi = Entry(window, textvariable=qval_bombe_crema_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_bombe_crema_pi.grid(row=4, column=9)

qval_bombe_cioc_pi = StringVar()
q_bombe_cioc_pi = Entry(window, textvariable=qval_bombe_cioc_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_bombe_cioc_pi.grid(row=5, column=9)

qval_fagot_cioc_pi = StringVar()
q_fagot_cioc_pi = Entry(window, textvariable=qval_fagot_cioc_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_fagot_cioc_pi.grid(row=6, column=9)

qval_fagot_mele_pi = StringVar()
q_fagot_mele_pi = Entry(window, textvariable=qval_fagot_mele_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_fagot_mele_pi.grid(row=7, column=9)

qval_fagot_bosco_pi = StringVar()
q_fagot_bosco_pi = Entry(window, textvariable=qval_fagot_bosco_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                         bd=3)
q_fagot_bosco_pi.grid(row=8, column=9)

qval_corn_crema_pi = StringVar()
q_corn_crema_pi = Entry(window, textvariable=qval_corn_crema_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                        bd=3)
q_corn_crema_pi.grid(row=9, column=9)

qval_corn_cioc_pi = StringVar()
q_corn_cioc_pi = Entry(window, textvariable=qval_corn_cioc_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_corn_cioc_pi.grid(row=10, column=9)

qval_corn_marm_pi = StringVar()
q_corn_marm_pi = Entry(window, textvariable=qval_corn_marm_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_corn_marm_pi.grid(row=11, column=9)

qval_corn_semp_pi = StringVar()
q_corn_semp_pi = Entry(window, textvariable=qval_corn_semp_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_corn_semp_pi.grid(row=12, column=9)

qval_inte_pi = StringVar()
q_inte_pi = Entry(window, textvariable=qval_inte_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                  bd=3)
q_inte_pi.grid(row=13, column=9)

qval_maritozzi_pi = StringVar()
q_maritozzi_pi = Entry(window, textvariable=qval_maritozzi_pi, width=6, font=FONT_LABEL, bg='#fafad2', fg='green',
                       bd=3)
q_maritozzi_pi.grid(row=14, column=9)

window.mainloop()

# use pyinstaller --onefile --window GeoLab_f.py
