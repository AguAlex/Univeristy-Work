
-- P1: Instanță ToFromArb pentru Point

-- Definirea tipurilor date:
data Point = Pt [Int] deriving Show
data Arb = Empty | Node Int Arb Arb deriving Show 

-- Clasă de tipuri ToFromArb:
class ToFromArb a where
    toArb :: a -> Arb
    fromArb :: Arb -> a

-- Funcție de inserare în arbore:
insertArb :: Int -> Arb -> Arb
insertArb x Empty = Node x Empty Empty
insertArb x (Node val left right)
    | x < val   = Node val (insertArb x left) right
    | otherwise = Node val left (insertArb x right)

-- Instanța ToFromArb pentru Point
instance ToFromArb Point where
    toArb (Pt xs) = foldr insertArb Empty xs
    fromArb Empty = Pt []
    fromArb (Node val left right) = 
        let Pt l = fromArb left
            Pt r = fromArb right
        in Pt (l ++ [val] ++ r)


-- P2: Funcția getFromInterval

-- Variante fără monade
getFromInterval :: Int -> Int -> [Int] -> [Int]
getFromInterval a b xs = filter (\x -> x >= a && x <= b) xs

-- Variantă cu monade
mGetFromInterval :: Int -> Int -> [Int] -> [Int]
mGetFromInterval a b xs = do
    x <- xs
    if x >= a && x <= b then return x else []

-- P3: Instanță Monad pentru ReaderWriter
newtype ReaderWriter env a = RW { getRW :: env -> (a, String) } 

instance Functor (ReaderWriter env) where
    fmap f (RW r) = RW (\env -> let (x, log) = r env in (f x, log))


instance Applicative (ReaderWriter env) where
    pure x = RW (\_ -> (x, ""))
    (RW f) <*> (RW x) = RW (\env -> 
        let (g, log1) = f env
            (y, log2) = x env
        in (g y, log1 ++ log2))

instance Monad (ReaderWriter env) where
    return = pure
    (RW r) >>= f = RW (\env -> 
        let (x, log1) = r env
            (RW r2) = f x
            (y, log2) = r2 env
        in (y, log1 ++ log2))







