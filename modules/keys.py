from enum import Enum;

from pygame.locals import *


class Keys(Enum):
    ESC="ESC"
    SPACE="SPACE"
    A="A"
    B="B"
    C="C"
    D="D"
    E="E"
    F="F"
    G="G"
    H="H"
    I="I"
    J="J"
    K="K"
    L="L"
    M="M"
    N="N"
    O="O"
    P="P"
    Q="Q"
    R="R"
    S="S"
    T="T"
    U="U"
    V="V"
    W="W"
    X="X"
    Y="Y"
    Z="Z"
    
    # PygameのkeyをKeysに変換
    @staticmethod
    def convert_key(pygame_key):
        keys_map={
            K_ESCAPE:Keys.ESC,
            K_SPACE:Keys.SPACE,
            K_a:Keys.A,
            K_b:Keys.B,
            K_c:Keys.C,
            K_d:Keys.D,
            K_e:Keys.E,
            K_f:Keys.F,
            K_g:Keys.G,
            K_h:Keys.H,
            K_i:Keys.I,
            K_j:Keys.J,
            K_k:Keys.K,
            K_l:Keys.L,
            K_m:Keys.M,
            K_n:Keys.N,
            K_o:Keys.O,
            K_p:Keys.P,
            K_q:Keys.Q,
            K_r:Keys.R,
            K_s:Keys.S,
            K_t:Keys.T,
            K_u:Keys.U,
            K_v:Keys.V,
            K_w:Keys.W,
            K_x:Keys.X,
            K_y:Keys.Y,
            K_z:Keys.Z,
        }
        
        return keys_map.get(pygame_key,None)
