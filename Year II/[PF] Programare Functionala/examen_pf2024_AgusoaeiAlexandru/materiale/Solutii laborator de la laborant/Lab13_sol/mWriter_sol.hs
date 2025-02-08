--5.
--- Monada Writer

newtype WriterS a = Writer { runWriter :: (a, String) }


instance  Monad WriterS where
  return va = Writer (va, "")
  ma >>= k = let (va, log1) = runWriter ma
                 (vb, log2) = runWriter (k va)
             in  Writer (vb, log1 ++ log2)


instance  Applicative WriterS where
  pure = return
  mf <*> ma = do
    f <- mf
    a <- ma
    return (f a)


instance  Functor WriterS where
  fmap f ma = pure f <*> ma


tell :: String -> WriterS ()
tell log = Writer ((), log)


--a)
logIncrement :: Int  -> WriterS Int
logIncrement x = do
  tell ( " increment : " ++ show x ++ " \n " )
  return (x+1)

logIncrement2 :: Int  -> WriterS Int
logIncrement2 x = do
    y <- logIncrement x
    logIncrement y

--test:
--runWriter $ logIncrement 2

--b)
logIncrementN :: Int -> Int -> WriterS Int
logIncrementN x 1 = logIncrement x
logIncrementN x n =  do
  y <- logIncrement x
  logIncrementN y (n-1)

--test:
--runWriter $ logIncrementN 2 4
--rezultat: (6," increment : 2 \n  increment : 3 \n  increment : 4 \n  increment : 5 \n ")

--c)
newtype WriterLS a = WriterLS {runWriterLS :: (a, [String])}


instance  Monad WriterLS where
  return va = WriterLS (va, [""])
  ma >>= k = let (va, log1) = runWriterLS ma
                 (vb, log2) = runWriterLS (k va)
             in  WriterLS (vb, log1 ++ log2)


instance  Applicative WriterLS where
  pure = return
  mf <*> ma = do
    f <- mf
    a <- ma
    return (f a)


instance  Functor WriterLS where
  fmap f ma = pure f <*> ma


tellLS :: String -> WriterLS ()
tellLS log = WriterLS ((), [log])


--redefinire functie logIncrementN:
logIncrement' :: Int  -> WriterLS Int
logIncrement' x = do
  tellLS ( " increment : " ++ show x )
  return (x+1)

logIncrementN' :: Int -> Int -> WriterLS Int
logIncrementN' x 1 = logIncrement' x
logIncrementN' x n =  do
  y <- logIncrement' x
  logIncrementN' y (n-1)

--test:
--runWriterLS $ logIncrementN' 2 4
--rezultat: (6,[" increment : 2",""," increment : 3",""," increment : 4",""," increment : 5",""])


--6.
data Person = Person { name :: String, age :: Int }

--b)
showPerson :: Person -> String
showPerson (Person name age) =
  let (_, log) = runWriter $ tell ("(NAME: " ++ name ++ ", AGE: " ++ show age ++ ")")
  in log

--test:
{-
showPerson $ Person "ada" 20
"(NAME: ada, AGE: 20)"
-}
