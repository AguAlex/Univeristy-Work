--1.
newtype Identity a = Identity a

instance Functor Identity where
  fmap f (Identity x) = Identity (f x)


--2.
data Pair a = Pair a a

instance Functor Pair where
  fmap f (Pair a1 a2) = Pair (f a1) (f a2)


--3.
data Constant a b = Constant b

instance Functor (Constant a) where
  fmap f (Constant b1) = Constant (f b1)


--4.
data Two a b = Two a b

instance Functor (Two a) where
  fmap f (Two a1 b1) = Two a1 (f b1)


--5.
data Three a b c = Three a b c

instance Functor (Three a b) where
  fmap f (Three a1 b1 c1) = Three a1 b1 (f c1)


--6.
data Three' a b = Three' a b b

instance Functor (Three' a) where
  fmap f (Three' a1 b1 b2) = Three' a1 (f b1) (f b2)


--7.
data Four a b c d = Four a b c d

instance Functor (Four a b c) where
  fmap f (Four a1 b1 c1 d1) = Four a1 b1 c1 (f d1)


--8.
data Four'' a b = Four'' a a a b

instance Functor (Four'' a) where
  fmap f (Four'' a1 a2 a3 b1) = Four'' a1 a2 a3 (f b1)


--9.
data Quant a b = Finance | Desk a | Bloor b

instance Functor (Quant a) where
  fmap _ Finance = Finance
  fmap _ (Desk a1) = Desk a1
  fmap f (Bloor b1) = Bloor (f b1)


--10.
data LiftItOut f a = LiftItOut (f a)

instance Functor f => Functor (LiftItOut f) where
  fmap fct (LiftItOut fa) = LiftItOut (fmap fct fa)


--11.
data Parappa f g a = DaWrappa (f a) (g a)

instance (Functor f, Functor g) => Functor (Parappa f g) where
  fmap fct (DaWrappa fa ga) = DaWrappa (fmap fct fa) (fmap fct ga)


--12.
data IgnoreOne f g a b = IgnoringSomething (f a) (g b)

instance (Functor g) => Functor (IgnoreOne f g a) where
  fmap fct (IgnoringSomething fa gb) = IgnoringSomething fa (fmap fct gb)


--13.
data Notorious g o a t = Notorious (g o) (g a) (g t)

instance (Functor g) => Functor (Notorious g o a) where
  fmap fct (Notorious ga gb gt) = Notorious ga gb (fmap fct gt)


--14.
data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)

instance Functor GoatLord where
  fmap fct = go
    where
      go NoGoat = NoGoat
      go (OneGoat a) = OneGoat (fct a)
      go (MoreGoats gl1 gl2 gl3) = MoreGoats (go gl1) (go gl2) (go gl3)


--15.
data TalkToMe a = Halt | Print String a | Read (String -> a)

instance Functor TalkToMe where
  fmap _ Halt = Halt
  fmap f (Print s1 a1) = Print s1 (f a1)
  fmap f (Read fsa) = Read (f . fsa)
