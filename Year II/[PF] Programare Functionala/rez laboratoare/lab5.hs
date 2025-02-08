--1
sumaPatrateImpare :: [Int] -> Int
sumaPatrateImpare lista = foldl (+) 0 (map (^2) (filter odd lista))

--2
toateTrue :: [Bool] -> Bool
toateTrue lista = foldr (&&) True lista

--3 ?????????????
-- allVerifies :: (Int -> Bool) -> [Int] -> Bool
-- allVerifies 

--4 ???????????????

--5
mapFoldr :: (a -> b) -> [a] -> [b]
mapFoldr expr l = foldr (\x l -> expr x : l) [] l

filterFoldr :: (a -> Bool) -> [a] -> [a]
filterFoldr expr l = foldr (\x l -> if expr x then x : l else l) [] l

--6
listToInt :: [Int] -> Int
listToInt lista = foldl (\x y -> 10*x + y) 0 lista

--7
rmChar :: Char -> String -> String
rmChar c cuv = [x | x <- cuv, x /= c]

rmCharsRec :: String -> String -> String
rmCharsRec [] _ = []
rmCharsRec (h:t) str = rmCharsRec t (rmChar h str)

--c
rmCharsFold :: String -> String -> String
rmCharsFold s1 s2 = foldr (\c l -> rmChar c l) s2 s1

--8
myReverse :: [Int] -> [Int]
myReverse l = foldl (\l x -> x : l) [] l

--9
myElem :: Int -> [Int] -> Bool
myElem x list = foldr (||) False (map (== x) list)

--10
myUnzip :: [(a, b)] -> ([a], [b])
myUnzip l = foldr (\(x, y) (xs, ys) -> (x : xs, y : ys)) ([], []) l

-- 11
union :: [Int] -> [Int] -> [Int]
union l1 l2 = foldr (\x y -> if (myElem x y) then y else x : y) l1 l2

-- 12
intersect :: [Int] -> [Int] -> [Int]
intersect l1 l2 = foldr (\x y -> if (myElem x l1) then x : y else y) [] l2

-- 13
pozitioneazaPesteTot :: Int -> [Int] -> [[Int]]
pozitioneazaPesteTot x l = foldr (\a y -> ((take a l) ++ (x : (reverse . take (length l - a) . reverse $ l))):y) [] [0..(length l)]

permutations :: [Int] -> [[Int]]
permutations [] = [[]]
permutations (p:ps) = foldr (\x y -> (pozitioneazaPesteTot p x) ++ y) [] (permutations ps)