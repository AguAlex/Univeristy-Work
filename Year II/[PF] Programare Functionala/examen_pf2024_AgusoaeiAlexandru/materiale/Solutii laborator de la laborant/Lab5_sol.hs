
--1.
sumImp :: [Int] -> Int
sumImp l = foldr (+) 0 (map (^2) (filter odd l ))


--2.
alltrue :: [Bool] -> Bool
alltrue l = foldr (&&) True l


--3.
allVerifies :: (Int -> Bool) -> [Int] -> Bool
allVerifies p list = foldr (\ x acc -> acc && p x) True list


--4.
anyVerifies :: (Int -> Bool) -> [Int] -> Bool
anyVerifies  p list = foldr (\ x acc -> acc || p x) False list


--5.
mapFoldr :: (a->b) -> [a] -> [b]
mapFoldr f list = foldr (\ x acc -> f x : acc) [] list

filterFoldr :: (a->Bool) -> [a] -> [a]
filterFoldr p list = foldr (\ x acc -> (if p x then [x] else [] ) ++ acc) [] list


--6.
listToInt :: [Integer]-> Integer
listToInt list = foldl (\acc x->acc * 10 + x) 0 list


--7.a
rmChar :: Char -> String -> String
rmChar c s = filter (/=c) s


--7.b
rmCharsRec :: String -> String -> String
rmCharsRec "" s2 = s2
rmCharsRec (c:s) s2 = rmCharsRec s (rmChar c s2)

--sau cu garzi
{- 
rmCharsRec :: String -> String -> String
rmCharsRec s1 "" = ""
rmCharsRec s1 (c:s)
   | c `elem` s1 = rmCharsRec s1 s
   | otherwise = c:rmCharsRec s1 s
-}


--7.c
rmCharsFold :: String -> String -> String
rmCharsFold s1 s2 = foldr (rmChar) s2 s1


--8.
myReverse :: [Int] -> [Int]
myReverse = foldr f e
  where
    f x r = r ++ [x]
    e     = []


--9.
myElem :: Int -> [Int] -> Bool
myElem y = foldr f e
  where
    f x r = (x == y) || r
    e = False
    

--10.
myUnzip :: [(a, b)] -> ([a], [b])
myUnzip = foldr f e
  where
    f (a,b) (as,bs) = (a:as,b:bs)
    e = ([],[])
    

--11.
union :: [Int] -> [Int] -> [Int]    
union xs ys = foldr f e ys
  where
    f y r | y `elem` xs = r
          | otherwise = r ++ [y]
    e = xs    
    

--12.
intersect :: [Int] -> [Int] -> [Int]      
intersect xs ys = foldr f e ys
  where
    f y r | y `elem` xs = y:r
          | otherwise   = r
    e = []


--13.
permutations :: [Int] -> [[Int]]
permutations = foldr f e
  where
    f x r = concatMap (insertAtAllPositions x) r
    e     = [[]]

--concatMap g = foldr f e
--  where
--    f x r = g x ++ r
--    e     = []

-- Functie care insereaza un element in toate pozitiile posibile intr-o lista
insertAtAllPositions :: a -> [a] -> [[a]]
insertAtAllPositions x [] = [[x]]
insertAtAllPositions x (y:ys) = (x:y:ys) : map (y:) (insertAtAllPositions x ys) 
     
--sau 
-- Functia permutations care foloseste foldr pentru a genera toate permutarile
--permutations :: [Int] -> [[Int]]
--permutations = foldr (\x acc -> foldr (++) [] (map (insertAtAllPositions x) acc)) [[]]