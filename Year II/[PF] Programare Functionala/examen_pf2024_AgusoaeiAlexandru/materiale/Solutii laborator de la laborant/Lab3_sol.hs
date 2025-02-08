import Data.Char

--1.a
verifL :: [Int] -> Bool
verifL l = even (length l)

--1.a
takefinal :: [Int] -> Int -> [Int]  
takefinal l n
  | length l > n = drop (length l - n) l
  | otherwise = l

--1.a
remove :: [a] -> Int -> [a]
remove l n = take n l ++ drop (n + 1) l


-- semiPare Rec [0,2,1,7,8,56,17,18] == [0,1,4,28,9]
semiPareRec :: [Int] -> [Int]
semiPareRec [] = []
semiPareRec (h:t)
 | even h    = h `div` 2 : t'
 | otherwise = t'
 where t' = semiPareRec t

--2.a
myreplicate :: Integer -> a -> [a]
myreplicate 0 v = []
myreplicate n v = v : myreplicate (n-1) v


--2.b
sumImp :: [Integer] -> Integer
sumImp [] = 0
sumImp (x:xs)
 | x `mod` 2 == 1 = x + sumImp xs
 | otherwise = sumImp xs


 --2.c 
totalLen :: [String] -> Int
totalLen [] = 0
totalLen (s:ss)
   | s !! 0 == 'A' = length s + totalLen ss
   | otherwise = totalLen ss


--3.
palindrom :: String -> Bool
palindrom s = s == reverse s

isVowel :: Char -> Bool
isVowel c = c `elem` "AEIOUaeiou"

countVowels :: String -> Int
countVowels "" = 0
countVowels (c:s) = (if isVowel c then 1 else 0 ) + countVowels s

nrVocale :: [String] -> Int
nrVocale [] = 0
nrVocale (s:ss)
  | palindrom s = countVowels s + nrVocale ss
  | otherwise = nrVocale ss


-- nrVocale ["sos", "civic", "palton", "desen", "aerisirea"] = 9


--4.
f :: Int -> [Int] -> [Int]
f _ [] = []
f y (x:xs)
  | x `mod` 2 == 0 = x:y: f y xs
  | otherwise = x: f y xs
-- f 3 [1,2,3,4,5,6] = [1,2,3,3,4,3,5,6,3]


semiPareComp :: [Int] -> [Int]
semiPareComp l = [ x `div` 2 | x <- l, even x ]

--5.
-- divizori 4 = [1,2,4]
divizori :: Int -> [Int]
divizori n = [d | d<-[1..n], n `mod` d == 0 ]


--6.
listadiv :: [Int] -> [[Int]]
listadiv l = [divizori n | n <- l]
-- listadiv [1,4,6,8] = [[1],[1,2,4],[1,2,3,6],[1,2,4,8]]

--7.a
inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec _ _ [] = []
inIntervalRec a b (x:xs)  = (if a <= x && x<=b then x:inIntervalRec a b xs else inIntervalRec a b xs)


--7.b
inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp a b l = [x | x<-l, a<=x && x<=b]
-- inInterval 5 10 [1..15] == [5,6,7,8,9,10]
-- inInterval 5 10 [1,3,5,2,8,-1] = [5,8]

--8.a
pozitiveRec :: [Int] -> Int
pozitiveRec [] = 0
pozitiveRec (x:xs)
  | x > 0 = 1 + pozitiveRec xs
  | otherwise = pozitiveRec xs


--8.b
pozitiveComp :: [Int] -> Int
pozitiveComp l = length [n | n<-l, n > 0]

-- pozitive [0,1,-3,-2,8,-1,6] == 3


--9.a
pozitiiImpareRec, pozitiiImpareComp :: [Int] -> [Int]

pozitiiImpareRecAux _ [] = []
pozitiiImpareRecAux i (x:xs)
    | x `mod` 2 == 1 = i : pozitiiImpareRecAux (i+1) xs
    | otherwise = pozitiiImpareRecAux (i+1) xs

pozitiiImpareRec l = pozitiiImpareRecAux 0 l

--9.b
pozitiiImpareComp l = [p | (el,p)<- zip l [0..], el `mod` 2 == 1]
-- pozitiiImpare [0,1,-3,-2,8,-1,6,1] == [1,2,5,7]

--10.a
multDigitsRec :: String -> Int
multDigitsRec "" = 1
multDigitsRec (c:s) = if isDigit  c then digitToInt c * multDigitsRec s
    else multDigitsRec s

--10.b
multDigitsComp :: String -> Int
multDigitsComp s = product [digitToInt c | c<-s, isDigit c]

-- multDigits "The time is 4:25" == 40
-- multDigits "No digits here!" == 1

--11. 
allPermutations :: Eq a => [a] -> [[a]]
allPermutations [] = [[]]
allPermutations xs = [y:zs | y <- xs, zs <- allPermutations (rmv xs y)]
  where
    rmv [] _ = []
    rmv (x:xs) y
      | x == y    = xs
      | otherwise = x : rmv xs y

--12.
combinations :: Int -> [a] -> [[a]]
combinations 0 _  = [[]]
combinations _ [] = []
combinations k (x:xs)
  | k < 0     = []
  | otherwise = [x:ys | ys <- combinations (k-1) xs] ++ combinations k xs


--13.
permutationsK :: Eq a => Int -> [a] -> [[a]]
permutationsK 0 _  = [[]]  -- Caz de baza: aranjamentele de 0 elemente sunt lista goala
permutationsK _ [] = []     -- Nu exista aranjamente daca lista este goala
permutationsK k xs = [x:ys | x <- xs, ys <- permutationsK (k-1) (rmv xs x)]
  where
    rmv [] _ = []
    rmv (y:ys) x
      | y == x    = ys
      | otherwise = y : rmv ys x

--14. Aici folosim backtracking
placeQueens :: Int -> Int -> [[(Int, Int)]]
placeQueens size numQueens = place numQueens [] 
  where
    place 0 positions = [positions]  -- Caz de baza: toate damele sunt plasate
    place k positions = 
      [ (row, col) : ps | col <- [0..size-1], 
                          row <- [0..size-1], 
                          safe (row, col) positions,
                          ps <- place (k-1) ((row, col):positions) ]

    safe (row, col) positions = all notAttacking positions
      where
        notAttacking (r, c) = r /= row && c /= col && abs (r - row) /= abs (c - col)

