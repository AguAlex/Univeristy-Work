data RGB v = RGB v v v
    deriving Show
newtype Image p = Img [[p]]
    deriving Show

class Composite c where
    blend :: (v -> v -> v) -> c (RGB v) -> c (RGB v) -> c (RGB v)

instance Composite Image where
    blend f (Img a) (Img b) =
        Img (zipWith (zipWith blendRGB) a b)
      where
        blendRGB (RGB r1 g1 b1) (RGB r2 g2 b2) =
            RGB (f r1 r2) (f g1 g2) (f b1 b2)

img1 = Img [[RGB 255 0 0, RGB 0 255 0, RGB 0 0 255]]
img2 = Img [[RGB 0 255 0, RGB 255 0 0, RGB 0 0 255]]


