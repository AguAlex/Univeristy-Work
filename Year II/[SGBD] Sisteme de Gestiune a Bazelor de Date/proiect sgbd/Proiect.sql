CREATE SEQUENCE seq
START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 30;

--PAROLE----------------------------------------------
CREATE TABLE parole
(
    parola_id number(5) constraint pk_parole primary key,
    parola_nume varchar(100) constraint parola_nume not null,
    nivel_securitate number(5) constraint securitate not null
);

INSERT INTO parole
VALUES (1, 'andrei2004', 5);

INSERT INTO parole
VALUES (2, 'asdasdasdasd', 7);

INSERT INTO parole
VALUES (3, '!Bucuresti2024', 9);

INSERT INTO parole
VALUES (4, '!AlexAvg 20', 10);

INSERT INTO parole
VALUES (5, 'tat', 2);

INSERT INTO parole
VALUES (6, 'Ianuarie2004', 8);

INSERT INTO parole
VALUES (7, 'a', 1);

INSERT INTO parole
VALUES (8, 'abc', 2);

INSERT INTO parole
VALUES (9, 'abc', 2);

INSERT INTO parole
VALUES (10, '!Ale 20', 9);

INSERT INTO parole
VALUES (11, '!AavFe', 8);

select *
from parole;

--ADRESE-------------------------------------------
CREATE TABLE adrese
(
    adresa_id number(5) constraint pk_adrese primary key,
    strada varchar(100) constraint strada not null,
    numar_strada number(5) constraint nr_strada not null,
    apartament number(5) constraint apartament not null
);

INSERT INTO adrese
VALUES (1, 'Aleea laleleor', 8, 12);

INSERT INTO adrese
VALUES (2, 'Aleea bratescu', 2, 3);

INSERT INTO adrese
VALUES (3, 'Aleea bratescu', 2, 23);

INSERT INTO adrese
VALUES (4, 'Aleea Drumul Taberei', 6, 1);

INSERT INTO adrese
VALUES (5, 'Aleea Arena', 11, 8);

INSERT INTO adrese
VALUES (6, 'Strada Balcescu', 4, 3);

select *
from adrese;

--LOCATII-----------------------------------------------
CREATE TABLE locatii
(
    locatie_id number(5) constraint pk_locatii primary key,
    adresa_id number(5),
    oras varchar(100) constraint oras not null,
    tara varchar(100) constraint tara not null,
    constraint fk_adresa FOREIGN KEY (adresa_id) REFERENCES adrese(adresa_id)
);

INSERT INTO locatii
VALUES (1, 1, 'Bucuresti', 'Romania');

INSERT INTO locatii
VALUES (2, 5, 'Bucuresti', 'Romania');

INSERT INTO locatii
VALUES (3, 2, 'Suceava', 'Romania');

INSERT INTO locatii
VALUES (4, 3, 'Atena', 'Grecia');

INSERT INTO locatii
VALUES (5, 4, 'Bucuresti', 'Romania');

INSERT INTO locatii
VALUES (6, 6, 'Brasov', 'Romania');

select *
from locatii;

--UTILIZATORI--------------------------------------------------------
CREATE TABLE utilizatori
(
    utilizator_id number(5) constraint pk_utilizator primary key,
    nume varchar(100) constraint nume_utilizator not null,
    prenume varchar(100) constraint prenume_utilizator not null,
    email varchar(100) constraint email_utilizator not null,
    parola_id number(5),
    locatie_id number(5),
    data_inregistrare date,
    constraint fk_parola FOREIGN KEY (parola_id) REFERENCES parole(parola_id),
    constraint fk_locatie FOREIGN KEY (locatie_id) REFERENCES locatii(locatie_id)
    
);

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Popescu', 'Andrei', 'popescu_andrei@gmail.com', 1, 1, TO_DATE('04/12/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Dimitrie', 'Roxana', 'dimitrie_roxx@gmail.com', 3, 4, TO_DATE('12/06/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Ionescu', 'Maria', 'ionescu_maria@gmail.com', 2, 2, TO_DATE('05/11/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Georgescu', 'Mihai', 'georgescu_mihai@gmail.com', 5, 3, TO_DATE('06/10/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Vasilescu', 'Elena', 'vasilescu_elena@gmail.com', 4, 3, TO_DATE('22/12/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (seq.NEXTVAL, 'Ionescu', 'Elena', 'ionescu_elena@gmail.com', 7, 2, TO_DATE('05/11/2023', 'DD/MM/YYYY'));

INSERT INTO utilizatori
VALUES (31, 'Mihailovici', 'Andrei', 'miha_andrei@gmail.com', 11, 6, TO_DATE('02/04/2023', 'DD/MM/YYYY'));

select *
from utilizatori;

--GRUPURI--------------------------------------------------------------------------
CREATE TABLE grupuri
(
    grup_id number(5) constraint pk_grup primary key,
    denumire varchar(100) constraint denumire_grup not null
);

INSERT INTO grupuri
VALUES (100, 'Scoala');

INSERT INTO grupuri
VALUES (101, 'La munca');

INSERT INTO grupuri
VALUES (102, 'Excursie');

INSERT INTO grupuri
VALUES (103, 'Grup');

INSERT INTO grupuri
VALUES (104, 'Prieteni');


select *
from grupuri;

--UTILIZATORI_SI_GRUPURI----------------------------------------------
CREATE TABLE utilizatori_si_grupuri
(
    utilizator_id number(5),
    grup_id number(5),
    constraint pk_util_gr primary key (utilizator_id, grup_id),
    constraint fk_utilizator foreign key (utilizator_id) references utilizatori(utilizator_id),
    constraint fk_grup foreign key (grup_id) references grupuri(grup_id)
);


INSERT INTO utilizatori_si_grupuri
VALUES (21, 100);

INSERT INTO utilizatori_si_grupuri
VALUES (22, 100);

INSERT INTO utilizatori_si_grupuri
VALUES (21, 101);

INSERT INTO utilizatori_si_grupuri
VALUES (23, 101);

INSERT INTO utilizatori_si_grupuri
VALUES (24, 101);

INSERT INTO utilizatori_si_grupuri
VALUES (25, 101);

INSERT INTO utilizatori_si_grupuri
VALUES (26, 101);

INSERT INTO utilizatori_si_grupuri
VALUES (31, 104);

INSERT INTO utilizatori_si_grupuri
VALUES (26, 104);

INSERT INTO utilizatori_si_grupuri
VALUES (23, 104);

INSERT INTO utilizatori_si_grupuri
VALUES (21, 104);

select *
from utilizatori_si_grupuri;

--FOTOGRAFII-------------------------------------------------
CREATE TABLE fotografii
(
    fotografie_id number(5) constraint pk_foto primary key,
    album_id number(5),
    titlu varchar(100) not null,
    constraint fk_album FOREIGN KEY (album_id) REFERENCES albume_fotografii(album_id)
);

INSERT INTO fotografii
VALUES (1, 100, 'Poza1');

INSERT INTO fotografii
VALUES (2, 100, 'Piscina');

INSERT INTO fotografii
VALUES (3, 100, 'Poza speciala');

INSERT INTO fotografii
VALUES (4, 101, 'Prima poza');

INSERT INTO fotografii
VALUES (5, 102, 'Rasarit');

INSERT INTO fotografii
VALUES (6, 102, 'La meci');

INSERT INTO fotografii
VALUES (7, 103, 'Poza Anglia');

INSERT INTO fotografii
VALUES (8, 104, 'Gratar');

select *
from fotografii;

--ALBUME_FOTOGRAFII-------------------------------------------------------------
CREATE TABLE albume_fotografii
(
    album_id number(5) constraint pk_album primary key,
    utilizator_id number(5),
    album_nume varchar(100) constraint nume_album not null,
    data_album date,
    constraint fk_util FOREIGN KEY (utilizator_id) REFERENCES utilizatori(utilizator_id)
);

INSERT INTO albume_fotografii
VALUES (100, 21, 'La mare', TO_DATE('25/12/2023', 'DD/MM/YYYY'));

INSERT INTO albume_fotografii
VALUES (101, 21, 'Ziua mea', TO_DATE('01/02/2024', 'DD/MM/YYYY'));

INSERT INTO albume_fotografii
VALUES (102, 23, 'Scoala', TO_DATE('29/11/2023', 'DD/MM/YYYY'));

INSERT INTO albume_fotografii
VALUES (103, 24, 'Facultate', TO_DATE('15/08/2023', 'DD/MM/YYYY'));

INSERT INTO albume_fotografii
VALUES (104, 24, 'La mare', TO_DATE('02/03/2024', 'DD/MM/YYYY'));

select *
from albume_fotografii;

--PIESE--------------------------------------------------------------
CREATE TABLE piese
(
    piesa_id number(5) constraint pk_piesa primary key,
    piesa_nume varchar(100) not null,
    artist_nume varchar(100) not null
);

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (1, 'Shape of You', 'Ed Sheeran');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (2, 'Blinding Lights', 'The Weeknd');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (3, 'Levitating', 'Dua Lipa');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (4, 'Bad Guy', 'Billie Eilish');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (5, 'Rockstar', 'Post Malone');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (6, 'Old Town Road', 'Lil Nas X');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (7, 'Senorita', 'Camila Cabello');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (8, 'Circles', 'Post Malone');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (9, 'Havana', 'Camila Cabello');

INSERT INTO piese (piesa_id, piesa_nume, artist_nume)
VALUES (10, 'My Eyes', 'Travis Scott');

select *
from piese;

--plylisturi_muzicale---------------------------------------------------------------
CREATE TABLE playlisturi_muzicale
(
    playlist_id number(5) constraint pk_playlist primary key,
    playlist_nume varchar(100) not null
);

INSERT INTO playlisturi_muzicale
VALUES (1, 'Piesele mele');

INSERT INTO playlisturi_muzicale
VALUES (2, 'Distractie');

INSERT INTO playlisturi_muzicale
VALUES (3, 'Relaxare');

INSERT INTO playlisturi_muzicale
VALUES (4, 'Alex Playlist');

INSERT INTO playlisturi_muzicale
VALUES (5, 'Dans');

select *
from playlisturi_muzicale;

--PLAYLISTURI_SI_PIESE-----------------------------------------------------------------
CREATE TABLE playlisturi_si_piese
(
    piesa_id number(5),
    playlist_id number(5),
    utilizator_id number(5),
    constraint pk_v_piese primary key (piesa_id, playlist_id, utilizator_id), --modificat pk
    constraint fk_utiliz foreign key (utilizator_id) REFERENCES utilizatori(utilizator_id),
    constraint fk_piesa foreign key (piesa_id) REFERENCES piese(piesa_id),
    constraint fk_playlist foreign key (playlist_id) REFERENCES playlisturi_muzicale(playlist_id)
);

INSERT INTO playlisturi_si_piese
VALUES (1, 1, 21);

INSERT INTO playlisturi_si_piese
VALUES (2, 1, 21);

INSERT INTO playlisturi_si_piese
VALUES (5, 1, 21);

INSERT INTO playlisturi_si_piese
VALUES (1, 2, 23);

INSERT INTO playlisturi_si_piese
VALUES (8, 3, 24);

INSERT INTO playlisturi_si_piese
VALUES (9, 3, 24);

INSERT INTO playlisturi_si_piese
VALUES (2, 3, 24);

INSERT INTO playlisturi_si_piese
VALUES (7, 4, 31);

INSERT INTO playlisturi_si_piese
VALUES (2, 4, 31);

INSERT INTO playlisturi_si_piese
VALUES (10, 2, 23);

select *
from playlisturi_si_piese;

--ISTORIC_PAROLE-----------------------------------------------------------------------
CREATE TABLE istoric_parole
(
    utilizator_id number(5),
    data_schimbare date,
    parola_id number(5),
    constraint pk_istoric primary key(utilizator_id, data_schimbare),
    constraint fk_parola_istoric foreign key (parola_id) references parole(parola_id)
);
 
INSERT INTO istoric_parole
VALUES (22, TO_DATE('27/12/2023', 'DD/MM/YYYY'), 8);

INSERT INTO istoric_parole
VALUES (22, TO_DATE('01/01/2024', 'DD/MM/YYYY'), 9);

INSERT INTO istoric_parole
VALUES (24, TO_DATE('30/12/2023', 'DD/MM/YYYY'), 10);
INSERT INTO istoric_parole
VALUES (31, TO_DATE('01/02/2024', 'DD/MM/YYYY'), 1);
INSERT INTO istoric_parole
VALUES (31, TO_DATE('04/02/2023', 'DD/MM/YYYY'), 3);
 
select *
from utilizatori;

--6 Afisare piese, playlisturi si grupuri pt un utilizator dat
set serveroutput on;
create or replace procedure ex6(
    utilizator_id_input utilizatori.utilizator_id%type  -- id-ul utilizatorului
)
is
    -- 1. colectie de tip tablou imbricat pentru piesele utilizatorului
    type colectie_piese is table of piese.piesa_nume%type;
    v_piese colectie_piese;

    -- 2. colectie de tip varray pentru playlisturile utilizatorului
    type colectie_playlisturi is varray(10) of playlisturi_muzicale.playlist_nume%type;
    v_playlisturi colectie_playlisturi;

    -- 3. colectie de tip tablou indexat pentru grupurile utilizatorului
    type colectie_grupuri is table of grupuri.denumire%type index by pls_integer;
    v_grupuri colectie_grupuri;

    -- numele utilizatorului
    nume_utilizator varchar2(20);
    prenume_utilizator varchar2(20);

begin
    -- obtinem numele utilizatorului
    select u.nume, u.prenume
    into nume_utilizator, prenume_utilizator
    from utilizatori u
    where u.utilizator_id = utilizator_id_input;

    -- afisam numele utilizatorului
    dbms_output.put_line('Numele utilizatorului: ' || nume_utilizator || ' ' || prenume_utilizator);

    -- 1. selectam piesele din playlisturile utilizatorului
    select distinct p.piesa_nume
    bulk collect into v_piese
    from piese p
    join playlisturi_si_piese pp on p.piesa_id = pp.piesa_id
    where pp.utilizator_id = utilizator_id_input;
    
    -- 2. selectam playlisturile utilizatorului
    select distinct pm.playlist_nume
    bulk collect into v_playlisturi
    from playlisturi_muzicale pm
    join playlisturi_si_piese pp on pm.playlist_id = pp.playlist_id
    where pp.utilizator_id = utilizator_id_input;
    
    -- 3. selectam grupurile utilizatorului
    select g.denumire
    bulk collect into v_grupuri
    from grupuri g
    join utilizatori_si_grupuri ug on g.grup_id = ug.grup_id
    where ug.utilizator_id = utilizator_id_input;
    
    dbms_output.put_line('Piese din playlisturile utilizatorului:');
    for i in 1..v_piese.count loop
        dbms_output.put_line('- ' || v_piese(i));
    end loop;

    dbms_output.put_line('Playlisturile utilizatorului:');
    for i in 1..v_playlisturi.count loop
        dbms_output.put_line('- ' || v_playlisturi(i));
    end loop;

    -- afisam grupurile din care face parte utilizatorul
    dbms_output.put_line('Grupurile din care face parte utilizatorul:');
    for i in 1..v_grupuri.count loop
        dbms_output.put_line('- ' || v_grupuri(i));
    end loop;

end ex6;
/

begin
    ex6(21);
end;
/

--7 Album si fiecare poza din album al utilizatorului

create or replace procedure ex7(
    p_utilizator_id utilizatori.utilizator_id%type
) is
    -- variabile pentru utilizator
    v_nume utilizatori.nume%type;
    v_prenume utilizatori.prenume%type;
    v_email utilizatori.email%type;

    -- cursor explicit pentru albume
    cursor albume_cursor is
        select album_id, album_nume, data_album
        from albume_fotografii
        where utilizator_id = p_utilizator_id;

    -- variabile pentru albume
    v_album_id albume_fotografii.album_id%type;
    v_album_nume albume_fotografii.album_nume%type;
    v_data_album albume_fotografii.data_album%type;

    -- cursor parametrizat pentru fotografii
    cursor fotografii_cursor(p_album_id fotografii.album_id%type) is
        select titlu
        from fotografii
        where album_id = p_album_id;

    -- variabila pentru fotografii
    v_titlu fotografii.titlu%type;

begin

    begin
        select nume, prenume, email
        into v_nume, v_prenume, v_email
        from utilizatori
        where utilizator_id = p_utilizator_id;
        
        dbms_output.put_line('Utilizator: ' || v_nume || ' ' || v_prenume || ' - ' || v_email);
    exception
        when no_data_found then
            dbms_output.put_line('Utilizatorul cu id-ul ' || p_utilizator_id || ' nu exista.');
            return;
    end;

    -- procesam albumele utilizatorului folosind cursorul explicit
    open albume_cursor;
    loop
        fetch albume_cursor into v_album_id, v_album_nume, v_data_album;
        exit when albume_cursor%notfound;

        dbms_output.put_line('Album: ' || v_album_nume || ' (data: ' || to_char(v_data_album, 'dd/mm/yyyy') || ')');

        -- procesam fotografiile asociate albumului curent
        open fotografii_cursor(v_album_id);
        loop
            fetch fotografii_cursor into v_titlu;
            exit when fotografii_cursor%notfound;
            dbms_output.put_line('- fotografie: ' || v_titlu);
        end loop;
        close fotografii_cursor;
    end loop;
    close albume_cursor;
end;
/

begin
    ex7(21);
end;
/

--8 Adresa completa a unui utilizator

create or replace function ex8(utilizator_id_input utilizatori.utilizator_id%type)
return varchar2
is
    adresa_completa varchar2(400);
begin
    
    select u.nume || ' ' || u.prenume || ' - ' ||
           a.strada || ', nr. ' || a.numar_strada || ', ap. ' || a.apartament
    into adresa_completa
    from utilizatori u
    join locatii l on u.locatie_id = l.locatie_id
    join adrese a on l.adresa_id = a.adresa_id
    where u.utilizator_id = utilizator_id_input;

    return adresa_completa;

exception
    when no_data_found then
        return 'Utilizatorul nu are o locatie asociata.';
    when too_many_rows then
        return 'Utilizatorul are mai multe locatii asociate.';
    when others then
        return 'Eroare necunoscuta';
end;
/

begin
    dbms_output.put_line(ex8(21));
end;
/

--9 Utilizator si album asociat, exceptii
select * from parole;
create or replace procedure ex9(
    p_utilizator_id utilizatori.utilizator_id%type,
    p_album_nume albume_fotografii.album_nume%type
)
is
    -- Declaratia exceptiilor proprii
    ex_utilizator_inexistent exception;
    ex_album_inexistent exception;

    -- Variabile pentru stocarea informatiilor utilizatorului
    v_nume_utilizator varchar2(200);
    v_email_utilizator varchar2(200);
    v_album_id albume_fotografii.album_id%type;

    -- Cursor complex care integreaza informatii din 5 tabele
    cursor detalii_cursor is
    select
        u.nume || ' ' || u.prenume as utilizator_nume,
        p.piesa_nume as piesa_nume,
        pa.parola_nume as parola,
        l.oras as locatie
    from utilizatori u
    join playlisturi_si_piese pp on u.utilizator_id = pp.utilizator_id
    join piese p on pp.piesa_id = p.piesa_id
    join parole pa on u.parola_id = pa.parola_id
    join locatii l on u.locatie_id = l.locatie_id
    where u.utilizator_id = p_utilizator_id;


    -- Variabile pentru cursor
    v_utilizator_nume varchar2(200);
    v_piesa_nume piese.piesa_nume%type;
    v_fotografie_titlu fotografii.titlu%type;
    v_album_nume albume_fotografii.album_nume%type;
    v_parola parole.parola_nume%type;
    v_oras locatii.oras%type;

begin
    -- Verificam daca utilizatorul exista
    begin
        select nume || ' ' || prenume, email
        into v_nume_utilizator, v_email_utilizator
        from utilizatori
        where utilizator_id = p_utilizator_id;

    exception
        when no_data_found then
            raise ex_utilizator_inexistent;
    end;

    -- Verificam daca albumul apartine utilizatorului
    begin
        select album_id
        into v_album_id
        from albume_fotografii
        where utilizator_id = p_utilizator_id
          and album_nume = p_album_nume;

    exception
        when no_data_found then
            raise ex_album_inexistent;
    end;

    -- Afisam informatiile
    dbms_output.put_line('Utilizator: ' || v_nume_utilizator || ' - ' || v_email_utilizator);

    dbms_output.put_line('Detalii piese:');
open detalii_cursor;
loop
    fetch detalii_cursor into v_utilizator_nume, v_piesa_nume, v_parola, v_oras;
    exit when detalii_cursor%notfound;

    dbms_output.put_line('Piesa: ' || v_piesa_nume);
    dbms_output.put_line('Oras: ' || v_oras);
    dbms_output.put_line('Parola: ' || v_parola);
    dbms_output.put_line('');
end loop;
close detalii_cursor;


exception
    when ex_utilizator_inexistent then
        dbms_output.put_line('Eroare: Utilizatorul cu ID-ul ' || p_utilizator_id || ' nu exista.');
    when ex_album_inexistent then
        dbms_output.put_line('Eroare: Albumul "' || p_album_nume || '" nu apartine utilizatorului specificat.');
    when others then
        dbms_output.put_line('A aparut o eroare.');
end;
/

begin
    ex9(999, 'La mare');
    ex9(21, 'qcnqeiq');
    ex9(21, 'La mare');
end;
/

-- lmd: select, insert, update, delete; ldd: create, alter, drop, truncate
--11 Trigger care updateaza istoricul de parole in functie de parolele schimbate
create or replace trigger trg_schimbare_parola
after update of parola_id on utilizatori
for each row
begin
    -- verificam daca parola s-a schimbat
    if :old.parola_id is not null and :new.parola_id != :old.parola_id then
        -- adaugam in istoric noua parola
        insert into istoric_parole (utilizator_id, data_schimbare, parola_id)
        values (:new.utilizator_id, sysdate, :new.parola_id);
    end if;
end;
/


SELECT * FROM istoric_parole;

UPDATE utilizatori
SET parola_id = 5
WHERE utilizator_id = 21;


--10 Inserare in aux_fotografii, numarul curent de fotografii dupa un insert in fotografii
create sequence seq_trigger
start with 1
increment by 1;

create table aux_fotografii (
    id number(5) primary key,
    numar_fotografii number(5) not null,
    data_operatie date default sysdate
);

create or replace trigger trg_insert_fotografii
after insert on fotografii
declare
    total_fotografii number;
begin
    select count(*)
    into total_fotografii
    from fotografii;

    insert into aux_fotografii (id, numar_fotografii, data_operatie)
    values (seq_trigger.nextval, total_fotografii, sysdate);
end;
/

insert into fotografii (fotografie_id, album_id, titlu) 
values (9, 104, 'Munte');

insert into fotografii (fotografie_id, album_id, titlu) 
values (10, 104, 'Apus');

select * from aux_fotografii;
select * from fotografii;
delete from fotografii where fotografie_id = 9 or fotografie_id = 10;

--12 Inserare info de modificare dupa alter piese

create sequence seq_aux_piese
start with 1
increment by 1;

create table aux_piese(
    id number(5) primary key,
    detalii varchar2(200)
);

create or replace trigger trg_alter_aux_piese
after alter on schema
begin
    insert into aux_piese(id, detalii)
    values (seq_aux_piese.nextval, 'Tabela PIESE a fost modificata');
end;
/
select * from piese;
alter table piese add coloana_auxiliara varchar(100);
alter table piese drop column coloana_auxiliara;
select * from aux_piese;

delete from aux_piese where id != -1;
rollback;

-- 13

create sequence seq_playlist
    start with 1
    increment by 1
    nocache;

create or replace package ex13_pachet as
    -- Pentru ID-urile pieselor
    type t_piese_imbricat is table of number;

    -- Pentru piesele unui playlist
    type t_piese_indexat is table of number index by pls_integer;

    -- Functie pentru obtinerea playlisturilor unui utilizator (pe baza ID-urilor pieselor)
    function obtine_playlisturi(utilizator_id_input number) return t_piese_imbricat;

    -- Functie pentru numararea pieselor dintr-un playlist
    function numara_piese(playlist_id_input number) return number;

    -- Procedura pentru adaugarea unui playlist nou (folosind ID-uri de piese)
    procedure adauga_playlist(utilizator_id_input number, playlist_nume_input varchar2, lista_piese t_piese_imbricat);

    -- Procedura pentru actualizarea pieselor dintr-un playlist (folosind ID-uri de piese)
    procedure actualizeaza_piese(playlist_id_input number, lista_piese t_piese_indexat);

end ex13_pachet;
/


create or replace package body ex13_pachet as

    function obtine_playlisturi(utilizator_id_input number) return t_piese_imbricat is
        playlisturi t_piese_imbricat;
    begin
        select ps.piesa_id
        bulk collect into playlisturi
        from playlisturi_si_piese ps
        where ps.utilizator_id = utilizator_id_input;

        return playlisturi;
    exception
        when no_data_found then
            return t_piese_imbricat();
        when others then
            return t_piese_imbricat();
    end;

    -- functia pentru numararea pieselor dintr-un playlist
    function numara_piese(playlist_id_input number) return number is
        total_piese number;
    begin
        select count(*)
        into total_piese
        from playlisturi_si_piese
        where playlist_id = playlist_id_input;

        return total_piese;
    exception
        when no_data_found then
            return 0;
        when others then
            return -1;
    end;

    -- procedura pentru adaugarea unui playlist nou (folosind ID-uri de piese)
    procedure adauga_playlist(utilizator_id_input number, playlist_nume_input varchar2, lista_piese t_piese_imbricat) is
        new_playlist_id number;
    begin
        -- adaugam playlistul in tabela playlisturi_muzicale
        select seq_playlist.nextval into new_playlist_id from dual;

        insert into playlisturi_muzicale (playlist_id, playlist_nume)
        values (new_playlist_id, playlist_nume_input);

        -- adaugam piesele asociate in tabela playlisturi_si_piese
        for i in 1 .. lista_piese.count loop
            insert into playlisturi_si_piese (piesa_id, playlist_id, utilizator_id)
            values (lista_piese(i), new_playlist_id, utilizator_id_input);
        end loop;

        dbms_output.put_line('Playlistul a fost adaugat cu succes.');
    exception
        when others then
            dbms_output.put_line('Eroare la adaugarea playlistului' || sqlerrm);
    end;

    -- procedura pentru actualizarea pieselor dintr-un playlist
    procedure actualizeaza_piese(playlist_id_input number, lista_piese t_piese_indexat) is
        utilizator_id_cautat number;
    begin
        -- Obtinem id-ul utilizatorului care detine playlist-ul
        select utilizator_id
        into utilizator_id_cautat
        from playlisturi_si_piese
        where playlist_id = playlist_id_input
        and rownum = 1;
    
        -- Stergem piesele existente din playlist
        delete from playlisturi_si_piese
        where playlist_id = playlist_id_input;
    
        -- Adaugam piesele noi
        for i in 1 .. lista_piese.count loop
            insert into playlisturi_si_piese (piesa_id, playlist_id, utilizator_id)
            values (lista_piese(i), playlist_id_input, utilizator_id_cautat);
        end loop;
    
        dbms_output.put_line('Playlistul a fost actualizat cu succes.');
    exception
        when no_data_found then
            dbms_output.put_line('Playlistul nu are niciun utilizator asociat.');
        when others then
            dbms_output.put_line('Eroare la actualizarea pieselor: ' || sqlerrm);
    end;


end ex13_pachet;
/

declare
    -- Crearea unui tablou imbricat pentru piesele playlistului nou
    piese_playlist_nou ex13_pachet.t_piese_imbricat := ex13_pachet.t_piese_imbricat(1, 2, 3, 4);

    -- Crearea unui tablou indexat pentru piesele playlistului actualizat
    piese_actualizate ex13_pachet.t_piese_indexat;
begin
    ex13_pachet.adauga_playlist(21, 'playlist nou', piese_playlist_nou);
    
    piese_actualizate(1) := 5;
    piese_actualizate(2) := 6;
    piese_actualizate(3) := 7;

    ex13_pachet.actualizeaza_piese(4, piese_actualizate); -- id playlist + id uri piese
end;
/
set serveroutput on;
select * from playlisturi_si_piese;
select * from playlisturi_muzicale;
select * from utilizatori;

delete from playlisturi_muzicale where playlist_nume like 'playlist nou';
delete from playlisturi_si_piese where playlist_id = 20;
