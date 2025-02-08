--1
data Expr = Var String | Val Int | Expr :+: Expr | Expr :*: Expr
    deriving (Show, Eq)

class Operations exp where
    simplify :: exp -> exp

instance Operations Expr where
    simplify (Var x) = Var x
    simplify (Val x) = Val x
    simplify ((Val 0) :+: ex) = simplify ex
    simplify ((Val 1) :*: ex) = simplify ex
    simplify (ex :+: (Val 0)) = simplify ex
    simplify (ex :*: (Val 1)) = simplify ex
    simplify (expr1 :+: expr2) = simplify expr1 :+: simplify expr2
    simplify (expr1 :*: expr2) = simplify expr1 :*: simplify expr2



ex3 = ((Val 0) :*: (Val 2)) :+: (Val 3)

--2
pasareasca :: String -> String
pasareasca "" = ""
pasareasca (h:t)
    | elem h "aeiouAEIOU" = h : 'p' : h : pasareasca t
    | otherwise = h : pasareasca t

--3
newtype ReaderM env a = ReaderM { runReaderM :: env -> Maybe a }

instance Monad (ReaderM env) where
    return x = ReaderM (\_ -> Just x)
    ma >>= k = ReaderM f where f env = case runReaderM ma env of
                                        Just a -> runReaderM (k a) env
                                        Nothing -> Nothing 

instance Applicative (ReaderM env)
instance Functor(ReaderM env)

testReaderM :: ReaderM String String
testReaderM = ma >>= k
    where
        ma =
            ReaderM
                (\ str -> if length str > 10 then Just (length str) else Nothing)
        k val =
            ReaderM
                (\ str -> if val `mod` 2 == 0 then Just "par" else Nothing)

main :: IO ()
main = do
    let result = runReaderM testReaderM "Hello, this is a long string"
    putStrLn $ "Result: " ++ show result