class Collection c where
  empty :: c key value
  singleton :: key -> value -> c key value
  insert
      :: Ord key
      => key -> value -> c key value -> c key value
  clookup :: Ord key => key -> c key value -> Maybe value
  delete :: Ord key => key -> c key value -> c key value
  keys :: c key value -> [key]
  values :: c key value -> [value]
  toList :: c key value -> [(key, value)]
  fromList :: Ord key => [(key,value)] -> c key value

--1.
  keys c = [fst p | p <- toList c]
  values c = [snd p | p <- toList c]
  fromList [] = empty
  fromList ((k,v):es)  = insert k v (fromList es)


--2.
newtype PairList k v = PairList { getPairList :: [(k, v)] }
  deriving Show

instance Collection PairList  where
   empty = PairList []
   singleton  k v = PairList [(k,v)]
   insert k v (PairList l) = PairList $ (k,v):filter ((/= k). fst) l
   clookup k = lookup k . getPairList
   delete k (PairList l) = PairList $ filter ((/= k). fst) l
   toList = getPairList

--Teste:
-- *Main> fromList [(1,"a"),(2,"b"),(3,"c")] :: PairList Int String
-- PairList [(1,"a"),(2,"b"),(3,"c")]

--3.   
data SearchTree key value
  = Empty
  | BNode
      (SearchTree key value) -- elemente cu cheia mai mica
      key                    -- cheia elementului
      (Maybe value)          -- valoarea elementului
      (SearchTree key value) -- elemente cu cheia mai mare
        deriving Show

instance Collection SearchTree where
   empty = Empty
   singleton k v = BNode Empty k (Just v) Empty
   insert k v = go
     where
       go Empty = singleton k v
       go (BNode t1 k1 v1 t2)
         | k == k1   = BNode t1 k1 (Just v) t2
         | k < k1    = BNode (go t1) k1 v1 t2
         | otherwise = BNode t1 k1 v1 (go t2)
   delete k = go
     where
       go Empty = Empty
       go (BNode t1 k1 v1 t2)
         | k == k1   = BNode t1 k1 Nothing t2
         | k < k1    = BNode (go t1) k1 v1 t2
         | otherwise = BNode t1 k1 v1 (go t2)
   clookup k = go
     where
       go Empty = Nothing
       go (BNode t1 k1 v1 t2)
         | k == k1   = v1
         | k < k1    = go t1
         | otherwise = go t2
   toList Empty = []
   toList (BNode ltk k v gtk) = toList ltk ++ embed k v ++ toList gtk
     where
       embed k (Just v) = [(k,v)]
       embed _ _ = []


--Teste:
-- *Main> fromList [(1,"a"),(2,"b"),(3,"c")] :: SearchTree Int String
-- Node (Node (Node Empty 1 (Just "a") Empty) 2 (Just "b") Empty) 3 (Just "c") Empty


--4.
data Punct = Pt [Int]

instance Show Punct where
  show (Pt []) = "()"
  show (Pt l) = "(" ++ parse l ++")"
     where
        parse [] = ""
        parse [x] = show x
        parse (x:y:xs) = show x ++ ", " ++ parse (y:xs)


--5.
--Frontiera unui arbore binar reprezinta multimea de noduri frunza din arbore
--Intr-un arbore binar, un nod este considerat frunza daca nu are niciun copil (adica subarborii sai stang si drept sunt null)

data Arb = Vid | F Int | N Arb Arb
          deriving Show

class ToFromArb a where
    toArb :: a -> Arb
    fromArb :: Arb -> a


instance ToFromArb Punct where
    toArb (Pt []) = Vid
    toArb (Pt (x:xs)) = N (F x) (toArb (Pt xs))
    fromArb (Vid) = Pt []
    fromArb (F x) = Pt [x]
    fromArb (N l r) = Pt (p1++p2)
      where  Pt p1 = fromArb l
             Pt p2 = fromArb r

--Teste:
-- toArb (Pt [1,2,3])
-- N (F 1) (N (F 2) (N (F 3) Vid))
-- fromArb $ N (F 1) (N (F 2) (N (F 3) Vid)) :: Punct
--  (1,2,3)


--6.
data Geo a = Square a | Rectangle a a | Circle a
    deriving Show

class GeoOps g where
  perimeter :: (Floating a) => g a -> a
  area :: (Floating a) =>  g a -> a

instance GeoOps Geo where
  perimeter (Square l) = 4 * l
  perimeter (Rectangle l1 l2) = 2*l1 + 2*l2
  perimeter (Circle r) = 2 * pi * r

  area (Square l) = l^2
  area (Rectangle l1 l2) = l1*l2
  area (Circle r) = pi * r^2

--7.
instance (Floating a, Eq a) => Eq (Geo a) where
     fig1 == fig2 = perimeter fig1 ==  perimeter fig2
