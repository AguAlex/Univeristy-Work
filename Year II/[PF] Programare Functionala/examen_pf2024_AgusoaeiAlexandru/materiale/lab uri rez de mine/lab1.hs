--1.
sumaPatrate :: Int -> Int -> Int
sumaPatrate x y = x*x + y*y

--2.
paritate :: Int -> String
paritate x = if even x then "par" else "impar"

--3
factorial :: Int -> Int
factorial 1 =  1
factorial 0 =  1
factorial x = x * factorial (x - 1)

--4
verificare :: Int -> Int -> String
verificare x y = if x > y*2 then "Da" else "Nu"

maxim :: [Int] -> Int
maxim [x] = x
maxim (x:rest) = max x (maxim rest)
