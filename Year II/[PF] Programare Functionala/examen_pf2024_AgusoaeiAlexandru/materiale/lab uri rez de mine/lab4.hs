
--2
factori :: Int -> [Int]
factori x = [d | d <- [1..x], x `rem` d == 0]

--3
prim :: Int -> Bool
prim x = if length (factori x) > 2 then False else True

--4
numerePrime :: Int -> [Int]
numerePrime n = [x | x <- [2..n], prim x == True]

--5 ???????????????
--myzip3 :: [Int] -> [Int] -> [Int] -> [(Int, Int, Int)]
--myzip3 l1 l2 l3 = zip (zip l1 l2) l3 

--6
firstEl :: [(a, b)] -> [a]
firstEl = map (\(x, y) -> x)

--7
sumList :: [[Int]] -> [Int]
sumList = map sum

--8
prel2 :: [Int] -> [Int]
prel2 = map (\x -> if x `rem` 2 == 0 then x`div`2 else x*2)

--9
fct :: Char -> [[Char]] -> [[Char]]
fct c = filter (elem c)

--10
fct10 :: [Int] -> [Int]
fct10 lista = map (^2) (filter odd lista)

--11
fct11 :: [Int] -> [Int]
fct11 lista = map (^2) (map (\(x, y) -> y) (filter (\(i, x) -> odd i) (zip [1..] lista)))

--12
numaiVocale :: [String] -> [String]
numaiVocale = map (filter (`elem` "aeiouAEIOU"))

--13

