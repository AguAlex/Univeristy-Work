--1
-- Tipul de date pentru punct
data Point = Pt [Int]
    deriving Show

-- Tipul de date pentru arbore binar de căutare
data Arb = Empty | Node Int Arb Arb
    deriving Show

-- Clasa ToFromArb
class ToFromArb a where
    toArb :: a -> Arb
    fromArb :: Arb -> a

-- Instanța clasei ToFromArb pentru Point
instance ToFromArb Point where
    -- Funcția toArb: Transformă un punct (o listă de coordonate) într-un arbore binar de căutare
    toArb (Pt []) = Empty  -- Punctul vid devine arbore gol
    toArb (Pt (x:xs)) = insert x (toArb (Pt xs))  -- Inserăm elementele una câte una în arbore

    -- Funcția fromArb: Transformă un arbore binar de căutare într-un punct (o listă de coordonate)
    fromArb Empty = Pt []  -- Arborele gol devine un punct vid
    fromArb (Node x left right) = Pt (inOrderTraversal left ++ [x] ++ inOrderTraversal right)

-- Funcție de inserare într-un arbore binar de căutare
insert :: Int -> Arb -> Arb
insert x Empty = Node x Empty Empty  -- Dacă arborele este gol, se adaugă elementul ca nod
insert x (Node value left right)
    | x < value = Node value (insert x left) right  -- Dacă x este mai mic decât valoarea curentă, îl punem în subarborele stâng
    | x > value = Node value left (insert x right)  -- Dacă x este mai mare decât valoarea curentă, îl punem în subarborele drept
    | otherwise = Node value left right  -- Dacă x este egal cu valoarea, nu facem nimic

-- Funcție pentru parcurgerea in-order a unui arbore
inOrderTraversal :: Arb -> [Int]
inOrderTraversal Empty = []  -- Arborele gol nu conține niciun element
inOrderTraversal (Node value left right) = inOrderTraversal left ++ [value] ++ inOrderTraversal right
