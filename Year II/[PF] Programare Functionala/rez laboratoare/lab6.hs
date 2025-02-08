--1
data Fruct
  = Mar String Bool
  | Portocala String Int

ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 = Portocala "Sanguinello" 10
cosFructe = [Mar "Ionatan" False,
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

--a
ePortocalaDeSicilia (Mar _ _) = False
ePortocalaDeSicilia (Portocala soi _)
    | soi == "Tarocco" || soi == "Moro" || soi == "Sanguinello" = True
    | otherwise = False

--b
nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia l = foldr (+) 0 (map(\(Portocala _ x) -> x) (filter ePortocalaDeSicilia l))

--c
areVierme :: Fruct -> Bool
areVierme (Mar _ True) = True
areVierme _ = False

nrMereViermi :: [Fruct] -> Int
nrMereViermi [] = 0
nrMereViermi (h:t)
    | areVierme h == True = 1 + nrMereViermi t
    | otherwise = nrMereViermi t

--2
type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
    deriving Show
    
--a
vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow!"
vorbeste (Caine _ _) = "Woof!"

--b
rasa :: Animal -> Maybe String
rasa (Pisica _) = Nothing
rasa (Caine _ a) = Just a

--3
data Linie = L [Int]
    deriving Show
data Matrice = M [Linie]
    deriving Show

--a
verifica :: Matrice -> Int -> Bool
verifica (M l) n = foldr (&&) True (map(==n) (map sum (map (\(L x) -> x) l)))

test_veri1 = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10
test_verif2 = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25

--b
doarPozN :: Matrice -> Int -> Bool
doarPozN (M l) n = foldr (&&) True (map (\(L x) -> foldr (&&) True (map (>0) x)) (filter (\(L x) -> length x == n) l))

testPoz1 = doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3
testPoz2 = doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3

--c
corect :: Matrice -> Bool
corect (M l) = foldr (&&) True (map (\(L x) -> length x == length (head (map (\(L x) -> x) l))) l)
testcorect1 = corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]])
testcorect2 = corect (M[L[1,2,3], L[4,5,8], L[3,6,8], L[8,5,3]])
