--1.
data Fruct
  = Mar String Bool
  | Portocala String Int

ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 = Portocala "Sanguinello" 10

listaFructe = [Mar "Ionatan" False,
                Portocala "Sanguinello" 10,
                Portocala "Valencia" 22,
                Mar "Golden Delicious" True,
                Portocala "Sanguinello" 15,
                Portocala "Moro" 12,
                Portocala "Tarocco" 3,
                Portocala "Moro" 12,
                Portocala "Valencia" 2,
                Mar "Golden Delicious" False,
                Mar "Golden" False,
                Mar "Golden" True]

--1.a
ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Portocala s i) = elem s ["Tarocco", "Moro", "Sanguinello"]
ePortocalaDeSicilia _ = False

test_ePortocalaDeSicilia1 =
    ePortocalaDeSicilia (Portocala "Moro" 12) == True
test_ePortocalaDeSicilia2 =
    ePortocalaDeSicilia (Mar "Ionatan" True) == False


--1.b
nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia list = sum[ i | Portocala s i <- list , ePortocalaDeSicilia (Portocala s i) ]

test_nrFeliiSicilia = nrFeliiSicilia listaFructe == 52


--1.c
nrMereViermi :: [Fruct] -> Int
nrMereViermi list = length [ b | Mar s b <- list , b ]

test_nrMereViermi = nrMereViermi listaFructe == 2


--2.
type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
    deriving Show

--2.a
vorbeste :: Animal -> String
vorbeste (Pisica _)= "Meow!"
vorbeste (Caine _ _) = "Woof!"


--2.b
rasa :: Animal -> Maybe String
rasa (Caine n r)= Just r
rasa _ = Nothing



--3.
data Linie = L [Int]
   deriving Show
data Matrice = M [Linie]
   deriving Show


--3.a
verifica :: Matrice -> Int -> Bool
verifica (M list) n =  foldr (&&) True (map (\ (L l)-> sum l == n ) list)

test_verif1 = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10 == False
test_verif2 = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25 == True


--3.b
doarPozN :: Matrice -> Int -> Bool
doarPozN (M list) n = foldr (&&) True (map pozitive liniiN)
    where
      liniiN = filter (\ (L l) -> length l == n) list
      pozitive (L l) = l == filter (> 0) l

testPoz1 = doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 == True

testPoz2 = doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 == False


--3.c

lungime :: Int -> Linie -> Bool
lungime lenFirst (L linie) = (length linie == lenFirst)
 
corect :: Matrice -> Bool
corect (M ( (L linie) : matrice) ) = all (\l -> lungime (length linie) l) matrice

--sau
{-
corect :: Matrice -> Bool
corect (M [])  = True
corect (M [l]) = True
corect (M (L l1: (L l2):list)) =  length l1 == length l2 && corect (M (L l2:list))
-}

testcorect1 = corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) == False
testcorect2 = corect (M[L[1,2,3], L[4,5,8], L[3,6,8], L[8,5,3]]) == True



--EXTRA
--4.

data Direction = North | East | South | West 
    deriving (Show, Enum, Eq)

--4.a
data Turtle = Turtle {
    position :: (Int, Int),
    direction :: Direction
} 
    deriving Show

{-
-- Mai sus, in definirea tipului de data Turtle, {} sunt folosite pentru a defini o inregistrare (record).
-- record-urile permit definirea unui tip de data ce contine campuri cu nume, facand mai usoara accesarea si modificarea campurilor componente ale tipului de data definit. 
--exemplu:
let myTurtle = Turtle { position = (0, 0), direction = North }
print (position myTurtle)  -- This will print "(0,0)"
print (direction myTurtle)  -- This will print "North"
-}


--putem defini tipul de data Turtle si fara sintaxa ce foloseste record: 
--data Turtle = Turtle (Int, Int) Direction 
--    deriving Show


--4.b
{-
data Action = Step | Turn 
    deriving Show
-}

moveTurtle :: Turtle -> Action -> Turtle
moveTurtle (Turtle (x, y) North) Step = Turtle (x, y + 1) North
moveTurtle (Turtle (x, y) East) Step  = Turtle (x + 1, y) East
moveTurtle (Turtle (x, y) South) Step = Turtle (x, y - 1) South
moveTurtle (Turtle (x, y) West) Step  = Turtle (x - 1, y) West
moveTurtle (Turtle pos dir) Turn      = Turtle pos (nextDirection dir)

nextDirection :: Direction -> Direction
nextDirection North = East
nextDirection East  = South
nextDirection South = West
nextDirection West  = North


--4.c
{-
data Command = Do Action | Repeat Int Action
    deriving Show
-}

--Pentru a executa un Command, vom scrie o functie executeCommand:
{-
executeCommand :: Turtle -> Command -> Turtle
executeCommand turtle (Do action) = moveTurtle turtle action
executeCommand turtle (Repeat n action) = iterate (`moveTurtle` action) turtle !! n
-}

--4.d
--Functie ce parcurge lista de comenzi si aplica fiecare comand asupra testoasei, intorcand pozitia finala a acesteia:
getPizza :: Turtle -> [Command] -> (Int, Int)
getPizza turtle [] = position turtle
getPizza turtle (cmd:cmds) = getPizza (executeCommand turtle cmd) cmds


--4.e 

--Pentru ca programul sa compileze, declaratiile de mai jos vor fi decomentate dupa ce declaratiile initiale ale
--tipurilor de date Command si Action si ale functiei executeCommand sunt comentate, pentru a nu aparea conflicte.
--Adaugam constructorii Wait si Seq pentru a trata noile tipuri de comenzi:

data Command = Do Action | Repeat Int Action | Wait | Seq Command Command 
    deriving Show
data Action = Step | Turn 
    deriving Show


--Actualizam functia executeCommand pentru a tine cont de noile comenzi Wait si Seq:

executeCommand :: Turtle -> Command -> Turtle
executeCommand turtle (Do action) = moveTurtle turtle action
executeCommand turtle (Repeat n action) = iterate (`moveTurtle` action) turtle !! n
executeCommand turtle Wait = turtle
executeCommand turtle (Seq c1 c2) = executeCommand (executeCommand turtle c1) c2


--4.f
--Vom agrega lista de comenzi folosind foldr cu Seq pentru a crea o comanda echivalenta:

combineCommands :: [Command] -> Command
combineCommands = foldr Seq Wait


--Exemplu testare:
main :: IO ()
main = do
    let turtle = Turtle (0, 0) North
    let commands = [Do Step, Do Turn, Repeat 3 Step, Wait, Seq (Do Step) (Do Turn)]
    print $ getPizza turtle commands

--in consola (in modul "ghci>") dam comanda "main"