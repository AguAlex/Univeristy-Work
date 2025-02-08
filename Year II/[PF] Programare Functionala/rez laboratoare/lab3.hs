--1 a
verifL :: [Int] -> Bool
verifL x = if even (length x) then True else False

--1 b
takefinal :: [Int] -> Int -> [Int]
takefinal l n = if length l <= n then l else drop (length l - n) l

--1 c
remove :: [Int] -> Int -> [Int]
remove l n = take (n-1) l ++ drop n l

--2 a
myreplicate :: Int -> Int -> [Int]
myreplicate 0 v = []
myreplicate n v = v : myreplicate (n - 1) v

--2 b
sumImp :: [Int] -> Int
sumImp [] = 0
sumImp (h:t)
   | odd h     = h + sumImp t
   | otherwise = sumImp t

--2 c
totalLen :: [String] -> Int
totalLen [] = 0
totalLen (h:t)
    | head h == 'A' = length h + totalLen t
    | otherwise     = totalLen t

--3
cntVowels :: String -> Int
cntVowels str = length [c | c <- str, isVowel c]
 where
    isVowel c = c `elem` "aeiouAEIOU"

nrVocale :: [String] -> Int
nrVocale [] = 0
nrVocale (h:t)
   | reverse h == h = cntVowels h + nrVocale t
   | otherwise      = nrVocale t

--4
f :: Int -> [Int] -> [Int]
f x [] = []
f x (h:t) = if even h then (h:x:f x t) else (h:f x t)

--5
divizori :: Int -> [Int]
divizori x = [nr | nr<-[1..x], x `mod` nr == 0]

--6
listadiv :: [Int] -> [[Int]]
--listadiv = map divizori
listadiv x = [divizori elem | elem <- x]

--7 b
-- inInterval :: Int -> Int -> [Int] -> [Int]
-- inInterval x y list = [z | z <- list, x <= z && z >= y]

--7 a
inInterval :: Int -> Int -> [Int] -> [Int]
inInterval x y (h:t) = if h >= x && x <= y
                         then h:inInterval x y t
                         else inInterval x y t
--8 a
pozitiveRec :: [Int] -> Int
pozitiveRec [] = 0
pozitiveRec (h:t) = if h > 0
                     then 1 + pozitiveRec t
                     else pozitiveRec t

--8 b
pozitive :: [Int] -> Int
pozitive list = length [x | x<-list, x>0]

--9 a
pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = aux l 0
  where
    aux [] _ = []
    aux (h:t) i
        | odd h     = i : aux t (i + 1)
        | otherwise = aux t (i + 1)

--9 b
pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp l = [i | (i, x) <- zip [0..] l, odd x]

--for
--[lista!!i | i <- [0..(length lista)-1], odd (lista!!i)]

