import sqlite3


def connect():
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS clienti (client_id INTEGER PRIMARY KEY, client_nume text)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS comenzi (comanda_id INTEGER PRIMARY KEY, nume_client text not null, ziua text not null, '
        'ciam int, bov int, boc int, boci int, canfrcr int, canfrci int, corngl int, cornsgl int, corncr int, '
        'cornci int, cornmarc int, cornmars int, corncibi int, fagci int, fagme int, rico int, fagbo int, '
        'camp int, campma int, danuv int, danci int, tregrzu int, trebn int, steuv int, raduv int, radci int, '
        'raduvscr int, radciscr int, vene int, mari int, canonzcr int, canonzci int, canocr int, canoci int, '
        'canobi int, ciamfo int, intngml int, intngmarsc int, intgelmi int, intspmi int, intsgel int, '
        'intgelsc int, intsemp int, canu int, canucr int, veg int, fazz int, roma int, ciampi int, bomvpi int, '
        'bomcrpi int, bomcipi int, fagpi int, fagmepi int, fagbospi int, corncrpi int, corncipi int, '
        'cornmarpi int, cornsempi int, intpi int, maripi int)')
    conn.commit()
    conn.close()


def adauga_client(client_nume):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO clienti VALUES (NULL,?)', (client_nume,))
    conn.commit()
    conn.close()


def adauga_comanda(nume_client, ziua, ciam, bov, boc, boci, canfrcr, canfrci, corngl, cornsgl, corncr, cornci,
                   cornmarc, cornmars, corncibi, fagci, fagme, rico, fagbo, camp, campma, danuv, danci, tregrzu,
                   trebn, steuv, raduv, radci, raduvscr, radciscr, vene, mari, canonzcr, canonzci, canocr, canoci,
                   canobi, ciamfo, intngml, intngmarsc, intgelmi, intspmi, intsgel, intgelsc, intsemp, canu, canucr,
                   veg, fazz, roma, ciampi, bomvpi, bomcrpi, bomcipi, fagpi, fagmepi, fagbospi, corncrpi, corncipi,
                   cornmarpi, cornsempi, intpi, maripi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO comenzi VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
        '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (nume_client, ziua, ciam, bov, boc, boci, canfrcr, canfrci, corngl, cornsgl, corncr, cornci, cornmarc,
         cornmars, corncibi, fagci, fagme, rico, fagbo, camp, campma, danuv, danci, tregrzu, trebn, steuv,
         raduv, radci, raduvscr, radciscr, vene, mari, canonzcr, canonzci, canocr, canoci, canobi, ciamfo,
         intngml, intngmarsc, intgelmi, intspmi, intsgel, intgelsc, intsemp, canu, canucr, veg, fazz, roma,
         ciampi, bomvpi, bomcrpi, bomcipi, fagpi, fagmepi, fagbospi, corncrpi, corncipi, cornmarpi, cornsempi,
         intpi, maripi,))
    conn.commit()
    conn.close()


def vizualizeaza_client():
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute('SELECT client_id, client_nume FROM clienti')
    rows = cli.fetchall()
    conn.close()
    return rows


def vizualizeaza_comanda(num):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT  comanda_id, nume_client, ziua, ciam, bov, boc, boci, canfrcr, canfrci, corngl, cornsgl, corncr, '
        'cornci, cornmarc, cornmars, corncibi, fagci, fagme, rico, fagbo, camp, campma, danuv, danci, tregrzu, trebn, '
        'steuv, raduv, radci, raduvscr, radciscr, vene, mari, canonzcr, canonzci, canocr, canoci, canobi, ciamfo, '
        'intngml, intngmarsc, intgelmi, intspmi, intsgel, intgelsc, intsemp, canu, canucr, veg, fazz, roma, ciampi, '
        'bomvpi, bomcrpi, bomcipi, fagpi, fagmepi, fagbospi, corncrpi, corncipi, cornmarpi, cornsempi, intpi, '
        'maripi  FROM comenzi WHERE nume_client=?',
        (num,))
    rows = cli.fetchall()
    conn.close()
    return rows


def sterge_client(id):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM clienti WHERE client_id=?', (id,))
    conn.commit()
    conn.close()


def sterge_comanda(id):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM comenzi WHERE comanda_id=?', (id,))
    conn.commit()
    conn.close()


def modifica_client(id, nume):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute('UPDATE clienti SET client_nume=? WHERE client_id=?', (nume, id,))
    conn.commit()
    conn.close()


def modifica_comanda(id, nume_client, ziua, ciam, bov, boc, boci, canfrcr, canfrci, corngl, cornsgl, corncr, cornci,
                     cornmarc, cornmars, corncibi, fagci, fagme, rico, fagbo, camp, campma, danuv, danci, tregrzu,
                     trebn, steuv, raduv, radci, raduvscr, radciscr, vene, mari, canonzcr, canonzci, canocr, canoci,
                     canobi, ciamfo, intngml, intngmarsc, intgelmi, intspmi, intsgel, intgelsc, intsemp, canu, canucr,
                     veg, fazz, roma, ciampi, bomvpi, bomcrpi, bomcipi, fagpi, fagmepi, fagbospi, corncrpi, corncipi,
                     cornmarpi, cornsempi, intpi, maripi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cur.execute(
        'UPDATE comenzi SET nume_client=?, ziua=?, ciam=?, bov=?, boc=?, boci=?, canfrcr=?, canfrci=?, corngl=?, '
        'cornsgl=?, corncr=?, cornci=?, cornmarc=?, cornmars=?, corncibi=?, fagci=?, fagme=?, rico=?, fagbo=?, camp=?, '
        'campma=?, danuv=?, danci=?, tregrzu=?, trebn=?, steuv=?, raduv=?, radci=?, raduvscr=?, radciscr=?, vene=?, '
        'mari=?, canonzcr=?, canonzci=?, canocr=?, canoci=?, canobi=?, ciamfo=?, intngml=?, intngmarsc=?, intgelmi=?, '
        'intspmi=?, intsgel=?, intgelsc=?, intsemp=?, canu=?, canucr=?, veg=?, fazz=?, roma=?, ciampi=?, bomvpi=?, '
        'bomcrpi=?, bomcipi=?, fagpi=?, fagmepi=?, fagbospi=?, corncrpi=?, corncipi=?, cornmarpi=?, cornsempi=?, '
        'intpi=?, maripi=? WHERE comanda_id=?',
        (nume_client, ziua, ciam, bov, boc, boci, canfrcr, canfrci, corngl, cornsgl, corncr, cornci, cornmarc,
         cornmars, corncibi, fagci, fagme, rico, fagbo, camp, campma, danuv, danci, tregrzu, trebn, steuv, raduv,
         radci, raduvscr, radciscr, vene, mari, canonzcr, canonzci, canocr, canoci, canobi, ciamfo, intngml,
         intngmarsc, intgelmi, intspmi, intsgel, intgelsc, intsemp, canu, canucr, veg, fazz, roma, ciampi, bomvpi,
         bomcrpi, bomcipi, fagpi, fagmepi, fagbospi, corncrpi, corncipi, cornmarpi, cornsempi, intpi, maripi, id))
    conn.commit()
    conn.close()


def calc_totale_cornetti(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(corngl) + SUM(cornsgl) + SUM(corncr) + SUM(cornci) + SUM(cornmarc) + SUM(cornmars) + '
        'SUM(corncibi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_bombe(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(bov) + SUM(boc) + SUM(boci)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_cann_fri(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(canfrcr) + SUM(canfrci)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_dan_uv(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(danuv)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_tre(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(tregrzu) + SUM(trebn)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_cano(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(canonzcr) + SUM(canonzci) + SUM(canocr) + SUM(canoci) + SUM(canobi)) FROM comenzi WHERE ziua=?',
        (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_integr(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(intngml) + SUM(intngmarsc) + SUM(intgelmi) + SUM(intspmi) + SUM(intsgel) + SUM(intgelsc) + '
        'SUM(intsemp)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_cann(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(canu) + SUM(canucr) + SUM(veg)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_corn_picc(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(corncrpi) + SUM(corncipi) + SUM(cornmarpi) + SUM(cornsempi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_bomb_picc(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(bomvpi) + SUM(bomcrpi) + SUM(bomcipi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_ciam(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(ciam)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagci(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagci)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagbo(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagbo)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagme(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagme)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_campa(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(campma) + SUM(camp)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_danci(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(danci)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_steuv(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(steuv)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_rade(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(raduv) + SUM(raduvscr)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_danci(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(danci)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_vene(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(vene)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_mari(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(mari)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_ciamfo(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(ciamfo)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fazz(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fazz)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_roma(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(roma)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_ciampi(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(ciampi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagpi(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagpi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagmepi(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagmepi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_fagbospi(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(fagbospi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_rico(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(rico)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


def calc_totale_intpi(zi):
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute(
        'SELECT (SUM(intpi)) FROM comenzi WHERE ziua=?', (zi,))
    rows = cli.fetchall()
    conn.close()
    return rows


# def calc_totale_fritti(zi):
#     conn = sqlite3.connect('geo_lab.db')
#     cur = conn.cursor()
#     cli = cur.execute(
#         'SELECT (SUM(ciam) + SUM(bov) + SUM(boc) + SUM(boci) + SUM(canfrcr) + SUM(canfrci)) FROM comenzi WHERE ziua=?',
#         (zi,))
#     rows = cli.fetchall()
#     conn.close()
#     return rows
#
#
# def calc_totale_fritti_picc(zi):
#     conn = sqlite3.connect('geo_lab.db')
#     cur = conn.cursor()
#     cli = cur.execute('SELECT (SUM(ciampi) + SUM(bomvpi) + SUM(bomcrpi) + SUM(bomcipi)) FROM comenzi WHERE ziua=?',
#                       (zi,))
#     rows = cli.fetchall()
#     conn.close()
#     return rows
#
#
# def calc_totale_picc(zi):
#     conn = sqlite3.connect('geo_lab.db')
#     cur = conn.cursor()
#     cli = cur.execute('SELECT (SUM(fagpi) + SUM(fagmepi) + SUM(fagbospi) + SUM(corncrpi) + SUM(corncipi) + '
#                       'SUM(cornmarpi) + SUM(cornsempi) + SUM(intpi) + SUM(maripi)) FROM comenzi WHERE ziua=?',
#                       (zi,))
#     rows = cli.fetchall()
#     conn.close()
#     return rows
#
#
# def calc_totale_grandi(zi):
#     conn = sqlite3.connect('geo_lab.db')
#     cur = conn.cursor()
#     cli = cur.execute('SELECT (SUM(corngl) + SUM(cornsgl) + SUM(corncr) + SUM(cornci) + SUM(cornmarc) + SUM(cornmars) '
#                       '+ SUM(corncibi) + SUM(fagci) + SUM(fagme) + SUM(rico) + SUM(fagbo) + SUM(camp) + SUM(campma) '
#                       '+ SUM(danuv) + SUM(danci) + SUM(tregrzu) + SUM(trebn) + SUM(steuv) + SUM(raduv) + SUM(radci) '
#                       '+ SUM(raduvscr) + SUM(radciscr) + SUM(vene) + SUM(mari) + SUM(canonzcr) + SUM(canonzci) '
#                       '+ SUM(canocr) + SUM(canoci) + SUM(canobi) + SUM(ciamfo) + SUM(intngml) + SUM(intngmarsc) '
#                       '+ SUM(intgelmi) + SUM(intspmi) + SUM(intsgel) + SUM(intgelsc) + SUM(intsemp) + SUM(canu) '
#                       '+ SUM(canucr) + SUM(veg) + SUM(fazz) + SUM(roma)) FROM comenzi WHERE ziua=?',
#                       (zi,))
#     rows = cli.fetchall()
#     conn.close()
#     return rows


def see_all_orders():
    conn = sqlite3.connect('geo_lab.db')
    cur = conn.cursor()
    cli = cur.execute('SELECT * FROM comenzi')
    rows = cli.fetchall()
    conn.close()
    return rows


connect()
# adauga_client('Stefan')
# adauga_comanda('George', 'Martedi', 2,3,6)
# adauga_comanda('Stefan', 'Lunedi', 2, 5, 7)
# sterge_client(4)
# sterge_comanda(10)
# modifica_client(2, 'George23')
# modifica_comanda(7, 'Stefan2323', 'mercoledi', 2, 5, 9)
# print((vizualizeaza_client()))
# print((vizualizeaza_comanda('George')))
# print(calc_totale_fritti_picc('Lunedi'))
# print(see_all_orders())
# sterge_comanda()
