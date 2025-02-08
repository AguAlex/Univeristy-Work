--6.a
sumaPatratelor :: Integer -> Integer -> Integer
sumaPatratelor x y = x^2 + y^2

--6.b
paritate :: Integer -> String
paritate x = if even x then "par" else "impar"

--6.c
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

--6.d
biggerThanDouble :: Integer -> Integer -> Bool
biggerThanDouble x y = x > 2 * y

--6.e
elementMaxim :: [Integer] -> Integer
elementMaxim [x] = x
elementMaxim (x:xs) = max x (elementMaxim xs)

--7.
poly :: Double -> Double -> Double -> Double -> Double
poly a b c x = a * x^2 + b * x + c

--8.
eeny :: Integer -> String
eeny x
 | x `mod` 2 == 0 = "eeny"
 | otherwise = "meeny"

--9.
fizzbuzz :: Integer -> String
fizzbuzz x
  | x `mod` 3 == 0 && x `mod` 5 == 0 = "FizzBuzz"
  | x `mod` 3 == 0 = "Fizz"
  | x `mod` 5 == 0 = "Buzz"
  | otherwise = ""


fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
    | n < 2     = n
    | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)
    
fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)
    

--10.    
tribonacciC :: Integer -> Integer
tribonacciC n
  | n <= 2 = 1
  | n == 3 = 2
  | n > 3 =  tribonacciC (n-1) + tribonacciC (n-2) + tribonacciC (n-3)

tribonacciEc :: Integer -> Integer
tribonacciEc 1 = 1
tribonacciEc 2 = 1
tribonacciEc 3 = 2
tribonacciEc n = tribonacciEc (n-1) + tribonacciEc (n-2) + tribonacciEc (n-3)


--11.
binomial :: Integer -> Integer -> Integer
binomial n 0 = 1
binomial 0 k = 0
binomial n k = binomial (n-1) k + binomial (n-1) (k-1)


