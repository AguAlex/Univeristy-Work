data Tree = Empty  -- arbore vid
   | Node Int Tree Tree Tree -- arbore cu valoare de tip Int in radacina si 3 fii
      
extree :: Tree
extree = Node 4 (Node 5 Empty Empty Empty) 
                (Node 3 Empty Empty (Node 1 Empty Empty Empty)) Empty

class ArbInfo t where
  level :: t -> Int -- intoarce inaltimea arborelui; pt un arbore vid se considera ca are inaltimea 0
  sumval :: t -> Int -- intoarce suma valorilor din arbore
  nrFrunze :: t -> Int -- intoarce nr de frunze al arborelui


--1.  
instance ArbInfo Tree where
  level Empty = 0
  level (Node x t1 t2 t3) = 1 + maximum [level t1, level t2, level t3]
  
  sumval Empty = 0
  sumval (Node x t1 t2 t3) =  x + sumval t1 + sumval t2 + sumval t3
  
  nrFrunze Empty = 0
  nrFrunze (Node x t1 t2 t3) 
    | level (Node x t1 t2 t3) == 1 = 1
    | otherwise = nrFrunze t1 + nrFrunze t2 + nrFrunze t3 
  
--Teste:
-- level extree
-- 3
-- sumval extree
-- 13
-- nrFrunze extree
-- 2


class Scalar a where
  zero :: a
  one :: a
  adds :: a -> a -> a
  mult :: a -> a -> a
  negates :: a -> a --calculeaza inversul aditiv in corp
  recips :: a -> a --calculeaza inversul multiplicativ in corp


--2.

--data Ratio a : Rational numbers, with numerator and denominator of some Integral type (https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-Ratio.html) 
--type Rational = Ratio Integer

--instance for Rational data type:
instance Scalar Rational where
  zero = 0
  one = 1
  adds = (+)
  mult = (*)
  negates = negate
  recips = recip

--instance for Double primitive data type:
instance Scalar Double where
  zero = 0
  one = 1
  adds = (+)
  mult = (*)
  negates = negate
  recips x = if x == 0 then error "Cannot divide by zero" else 1 / x


class (Scalar a) => Vector v a where
  zerov :: v a
  onev :: v a
  addv :: v a -> v a -> v a -- adunare vector
  smult :: a -> v a -> v a  -- inmultire cu scalare
  negatev :: v a -> v a -- negare vector


--3.
data V2D a = V2D a a
           deriving Show
             
instance (Scalar a) => Vector V2D a where
  zerov = V2D zero zero
  onev = V2D one one
  addv (V2D x1 y1) (V2D x2 y2) = V2D (adds x1 x2) (adds y1 y2)
  smult a (V2D x y) = V2D (mult a x) (mult a y)
  negatev (V2D x y) = V2D (negates x) (negates y)
    
data V3D a = V3D a a a
           deriving Show    

instance (Scalar a) => Vector V3D a where
  zerov = V3D zero zero zero
  onev = V3D one one one
  addv (V3D x1 y1 z1) (V3D x2 y2 z2) = V3D (adds x1 x2) (adds y1 y2) (adds z1 z2)
  smult a (V3D x y z) = V3D (mult a x) (mult a y) (mult a z)
  negatev (V3D x y z) = V3D (negates x) (negates y) (negates z)

--Teste:
-- addv (V2D (toRational 0) (toRational 0)) (V2D (toRational 1) (toRational 1))
-- addv (V3D (toRational 0) (toRational 0) (toRational 0)) (V3D (toRational 1) (toRational 1) (toRational 1))
-- addv (V3D 0 0 0) (V3D 1 1 1)
-- smult 2 (V3D 1 2 1)