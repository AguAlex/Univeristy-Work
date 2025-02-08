-- fara monade
-- fac o lista cu elementele care respecta conditia <n si >m
verificareElementeInterval :: [Int] -> Int -> Int -> [Int]
verificareElementeInterval l n m = filter (\x -> x < n || x > m) l

p1 :: [[Int]] -> Int -> Int -> [Int]
p1 [] _ _ = []
p1 (h:t) n m
    | ((length h) `rem` 2 == 1) && (length (verificareElementeInterval h n m) == length h) = h ++ p1 t n m --verific conditia de adaugare
    | otherwise = p1 t n m

-- cu monade

-- p1m :: [[Int]] -> Int -> Int -> [Int]
-- p1m (h:t) n m = do
--     x <- h
--     if ((length x) `rem` 2 == 1) && (length (verificareElementeInterval h n m) == length x) return (x ++ (p1m t n m)) else p1m t n m