import Data.Maybe

data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
          deriving Eq
data Operation = Add | Mult
         deriving (Eq, Show)
data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)

instance Show Expr where
  show (Const x) = show x
  show (e1 :+: e2) = "(" ++ show e1 ++ " + "++ show e2 ++ ")"
  show (e1 :*: e2) = "(" ++ show e1 ++ " * "++ show e2 ++ ")"


--1.
evalExp :: Expr -> Int
evalExp (Const c) = c
evalExp (e1 :+: e2) = evalExp e1 + evalExp e2
evalExp (e1 :*: e2) = evalExp e1 * evalExp e2

exp1 = ((Const 2 :*: Const 3) :+: (Const 0 :*: Const 5))
exp2 = (Const 2 :*: (Const 3 :+: Const 4))
exp3 = (Const 4 :+: (Const 3 :*: Const 3))
exp4 = (((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2)
test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16


--2.
evalArb :: Tree -> Int
evalArb (Lf x) = x
evalArb (Node Add st dr) = evalArb st + evalArb dr
evalArb (Node Mult st dr) = evalArb st * evalArb dr

arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)

test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16


--3.
expToArb :: Expr -> Tree
expToArb (Const x) = Lf x
expToArb (e1 :+: e2) = Node Add (expToArb e1) (expToArb e2)
expToArb (e1 :*: e2) = Node Mult (expToArb e1) (expToArb e2)

data IntSearchTree value
  = Empty
  | BNode
      (IntSearchTree value)    -- elemente cu cheia mai mica
      Int                       -- cheia elementului
      (Maybe value)             -- valoarea elementului
      (IntSearchTree value)    -- elemente cu cheia mai mare
  

--Exemplu folosit la testari:
exampleTree :: IntSearchTree String
exampleTree = 
  BNode 
    (BNode Empty 1 (Just "A") Empty)  -- Subarbore stang: cheia 1 -> "A"
    3 (Just "B")                     -- Radacina: cheia 3 -> "B"
    (BNode Empty 5 Nothing Empty)    -- Subarbore drept: cheia 5 -> Nothing (sters)

--4.  
lookup' :: Int -> IntSearchTree value -> Maybe value
lookup' _ Empty = Nothing  -- Daca arborele este gol, returneaza Nothing
lookup' key (BNode left nodeKey nodeValue right)
  | key < nodeKey = lookup' key left  -- Cauta in subarborele stang
  | key > nodeKey = lookup' key right -- Cauta în subarborele drept
  | otherwise     = nodeValue        -- Daca cheia este gasita, returneaza valoarea

--Teste:
test4_1  = lookup' 1 exampleTree == Just "A"  -- Gaseste cheia 1
test4_2 = lookup' 2 exampleTree == Nothing  -- Cheia 2 nu exista in arbore


--5.
--Vom face o parcurgere in-order (stanga, radacina, dreapta), deoarece aceasta pastreaza ordinea cheilor in arbore
keys :: IntSearchTree value -> [Int]
keys Empty = []  -- Daca arborele este gol, nu sunt chei
keys (BNode left nodeKey _ right) = keys left ++ [nodeKey] ++ keys right  -- Cheile din stanga + cheia nodului curent + cheile din dreapta

--Teste:
test5_1 = keys Empty == []                 --Arbore gol
test5_2 = keys exampleTree == [1, 3, 5] --Cheile arborelui exampleTree


--6.
--Deoarece valorile nodurilor sunt de tipul Maybe value, vom include in lista doar valorile existente (Just value) 
--si vom ignora nodurile marcate ca sterse (Nothing).
values :: IntSearchTree value -> [value]
values Empty = []  -- Daca arborele este gol, lista valorilor este goala
values (BNode left _ nodeValue right) = values left ++ maybeToList nodeValue ++ values right -- Valorile din stanga ++ valoarea curenta (daca exista) ++ valorile din dreapta
  where
    maybeToList :: Maybe value -> [value]
    maybeToList Nothing  = []     -- Daca valoarea este Nothing, ignoram nodul
    maybeToList (Just v) = [v]    -- Daca valoarea este Just v, includem v in listă

--Teste:
test6_1 = values Empty            -- Arbore gol => trebuie sa intoarca o lista goala
test6_2 = values exampleTree == ["A", "B"]   -- Valorile arborelui exampleTree


--7.
insert :: Int -> value -> IntSearchTree value -> IntSearchTree value
insert key val Empty = 
  BNode Empty key (Just val) Empty  -- Adauga un nod ca radacina intr-un arbore gol
insert key val (BNode left nodeKey nodeValue right)
  | key < nodeKey = BNode (insert key val left) nodeKey nodeValue right  -- Adauga recursiv in subarborele stang
  | key > nodeKey = BNode left nodeKey nodeValue (insert key val right)  -- Adauga recursiv in subarborele drept
  | otherwise = BNode left nodeKey (Just val) right  -- Actualizeaza valoarea daca cheia exista deja

--Teste:
--Inserare intr-un arbore gol
tree1 = insert 2 "C" Empty -- keys tree1 ar trebuie sa afiseze: [2], iar values tree1 ar trebuie sa afiseze: ["C"]
test7_1 = (keys tree1 == [2] &&  values tree1 == ["C"])
--Inserare intr-un arbore existent
tree2 = insert 2 "C" exampleTree  -- Cheile trebuie sa includa 2, iar valorile trebuie sa includă "C"
test7_2 = (keys tree2 == [1, 2, 3, 5] &&  values tree2 == ["A", "C", "B"])

--Actualizare valoare pentru o cheie existentă
tree3 = insert 3 "D" exampleTree -- Cheile raman neschimbate, iar valoarea pentru cheia 3 devine "D"
test7_3 = (keys tree3 == [1, 3, 5] && values tree3 == ["A", "D"])   


--8.
exampleTree2 :: IntSearchTree String
exampleTree2 = 
  BNode 
    (BNode Empty 1 (Just "A") Empty)  -- Subarbore stâng: cheia 1 -> "A"
    3 (Just "B")                     -- Rădăcină: cheia 3 -> "B"
    (BNode Empty 5 (Just "C") Empty) -- Subarbore drept: cheia 5 -> "C"

delete :: Int -> IntSearchTree value -> IntSearchTree value
delete _ Empty = Empty  -- Daca arborele este gol, nu este nimic de sters
delete key (BNode left nodeKey nodeValue right)
  | key < nodeKey = BNode (delete key left) nodeKey nodeValue right  -- Cauta recursiv in subarborele stang
  | key > nodeKey = BNode left nodeKey nodeValue (delete key right)  -- Cauta recursiv in subarborele drept
  | otherwise = BNode left nodeKey Nothing right  -- Marcheaza nodul curent ca sters

--Test:
--Stergere din arborele gol
test8_1 = delete 1 Empty --ar trebui sa afiseze "Empty", daca ar avea instantiere a clasei Show

--Stergere a unei chei care exista
tree4 = delete 3 exampleTree2 -- Cheile raman neschimbate, iar valoarea pentru cheia 3 este eliminata
test8_2 = (keys tree4 == [1, 3, 5] && values tree4 == ["A", "C"])  

--Stergere a unei chei care nu exista
tree5 = delete 4 exampleTree2 -- Cheile raman neschimbate, iar valorile raman neschimbate
test8_3 = (keys tree5 == [1, 3, 5] && values tree5 == ["A", "B", "C"])  


--9.
exampleTree3 :: IntSearchTree String
exampleTree3 = 
  BNode 
    (BNode Empty 1 (Just "A") Empty)  -- Subarbore stâng: cheia 1 -> "A"
    3 (Just "B")                     -- Rădăcină: cheia 3 -> "B"
    (BNode Empty 5 Nothing Empty)    -- Subarbore drept: cheia 5 -> Nothing (șters)

toList :: IntSearchTree value -> [(Int, value)]
toList Empty = []  -- Daca arborele este gol, lista este goala
toList (BNode left nodeKey nodeValue right) = 
  toList left ++ (case nodeValue of
                    Just v -> [(nodeKey, v)]  -- Daca valoarea exista, adaugam cheia si valoarea
                    Nothing -> [])  -- Daca valoarea este Nothing, nu adaugam nimic
  ++ toList right  -- Continuam cu subarborele drept

--Teste:
--Test pentru arbore gol
test9_1 = toList Empty  -- Arbore gol, va intoarce o lista goala

--Test pentru arbore cu elemente
test9_2 = toList exampleTree3 == [(1, "A"), (3, "B")] -- Cheile 1 si 3 cu valorile "A" și "B", iar cheia 5 este ignorata deoarece valoarea este Nothing


--10.
fromList :: [(Int, value)] -> IntSearchTree value
fromList [] = Empty  -- Daca lista este goala, arborele este gol
fromList ((key, value):xs) = insert key value (fromList xs)

--Teste:
exampleList :: [(Int, String)]
exampleList = [(1, "A"), (3, "B"), (5, "C")]
tree6 = fromList exampleList
test10_1 = (keys tree6 == [1, 3, 5]  && values tree6 == ["A", "B", "C"])-- Cheile din arborele generat trebuie sa fie [1, 3, 5], iar valorile corespunzatoare cheilor trebuie sa fie ["A", "B", "C"]


--11.
printTree :: IntSearchTree value -> String
printTree Empty = ""  -- Arborele gol este reprezentat prin string-ul vid
printTree (BNode left nodeKey nodeValue right) = 
  let leftStr = printTree left
      rightStr = printTree right
  in (if leftStr /= "" then "(" ++ leftStr ++ ") " else "") ++ show nodeKey ++
     (if rightStr /= "" then " (" ++ rightStr ++ ")" else "")

--Test:
exampleTree4 :: IntSearchTree String
exampleTree4 = 
  BNode 
    (BNode Empty 1 (Just "A") Empty)  -- Subarbore stang: cheia 1
    2 (Just "B")                     -- Radacina: cheia 2
    (BNode Empty 3 (Just "C") Empty)  -- Subarbore drept: cheia 3
test11_1 = printTree exampleTree4 == "(1) 2 (3)" 

--12. EXTRA
-- balance :: IntSearchTree value -> IntSearchTree value
-- balance = undefined

{-
      
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

  keys c = [fst p | p <- toList c]
  values c = [snd p | p <- toList c]
  fromList [] = empty
  fromList ((k,v):es)  = insert k v (fromList es)



newtype PairList k v = PairList { getPairList :: [(k, v)] }
  deriving Show


instance Collection PairList  where
   empty = PairList []
   singleton  k v = PairList [(k,v)]
   insert k v (PairList l) = PairList $ (k,v):filter ((/= k). fst) l
   clookup k = lookup k . getPairList
   delete k (PairList l) = PairList $ filter ((/= k). fst) l
   toList = getPairList
   
   
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


-- *Main> fromList [(1,"a"),(2,"b"),(3,"c")] :: PairList Int String
-- PairList [(1,"a"),(2,"b"),(3,"c")]
-- *Main> fromList [(1,"a"),(2,"b"),(3,"c")] :: SearchTree Int String
-- Node (Node (Node Empty 1 (Just "a") Empty) 2 (Just "b") Empty) 3 (Just "c") Empty

-}

