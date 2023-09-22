using Plots
using Random

function corriger(t::Float64)
    """ Corrige t (positif) dans [0, 1]."""
    return t - floor(Int, t)
end

mutable struct Forme
  x_::Any
  y_::Any
  nom_::String
end

""" x(t) de cette Forme. """
get_x(forme::Forme, t::Float64) = forme.x_(corriger(t))

""" y(t) de cette Forme. """
get_y(forme::Forme, t::Float64) = forme.y_(corriger(t))

""" Nom de cette Forme. """
nom(forme::Forme) = forme.nom_


function dessiner(forme::Forme)
    """ Dessine la forme. """
    nb_points = 1000
    ts = [i/nb_points for i in 1:nb_points+1]
    xs = [get_x(forme, t) for t in ts]
    ys = [get_y(forme, t) for t in ts]
    x_min = minimum(xs)
    x_max = maximum(xs)
    y_min = minimum(ys)
    y_max = maximum(ys)
    dx = (x_max - x_min)*0.05
    dy = (y_max - y_min)*0.05
    plot(xs, ys, legend=false, linewidth=2.0, aspect_ratio=:equal, grid=false,
        xlimits=(x_min-dx, x_max+dx), ylimits=(y_min-dy, y_max+dy))
end

function dessiner(forme::Forme, ligne::Tuple{Float64, Float64})
    """ Dessine la forme et ajoute la ligne indiquée (couple (t1, t2)). """
    dessiner(forme)
    plot!([get_x(forme, ligne[1]), get_x(forme, ligne[2])],
        [get_y(forme, ligne[1]), get_y(forme, ligne[2])],
        linewidth=1.0)
end


## -----------------------------------------------------------------------------
## Formes de base
## -----------------------------------------------------------------------------
function cercle(rayon::Float64)
    """ Renvoie un cercle du rayon indiqué. """
    return Forme(t -> rayon*cos(t*2*π),
                 t -> rayon*sin(t*2*π),
                 "cercle($rayon)")
end

## -----------------------------------------------------------------------------
function rectangle(cote1::Float64, cote2::Float64)
    """ Renvoie un rectangle avec les cotes indiquées. """
    function x_rect(t)
        t < 0.25 && return 4*cote1*t
        t < 0.50 && return cote1
        t < 0.75 && return cote1 - 4*cote1*(t-0.5)
        return 0.0
    end
    function y_rect(t)
        t < 0.25 && return 0
        t < 0.50 && return 4*cote2*(t-0.25)
        t < 0.75 && return cote2
        return cote2 - 4*cote2*(t-0.75)
    end
    return Forme(x_rect, y_rect, "rectangle($cote1, $cote2)")
end

## -----------------------------------------------------------------------------
function patate(s::Int64, complexite::Int64 = -1)
    """ Renvoie une patate de numéro s, et de complexité donnée. """
    funcs = [
        t -> cos(t*2*π),
        t -> sin(t*2*π),
        t -> 4*(0.5-t)^2,
        t -> 25/3*abs(0.5-t)^3,
        t -> exp(-25*(t-0.5)^2),
        t -> cos(t*10*π)/10,
        t -> sin(t*12*π)/15
    ]
    if complexite > 0
        funcs = funcs[1:complexite]
    end

    Random.seed!(s)
    cx = rand(Float64, (length(funcs),1))
    cy = rand(Float64, (length(funcs),1))
    return Forme(
        t -> sum([cx[i] * funcs[i](t) for i in 1:length(funcs)]),
        t -> sum([cy[i] * funcs[i](t) for i in 1:length(funcs)]),
        "patate($s, complexite=$complexite)")
end

## -----------------------------------------------------------------------------
## Transformations de formes
## -----------------------------------------------------------------------------
function transformer(forme::Forme, A::Matrix{Float64})
    """ Renvoie une nouvelle forme, transformée par la matrice A"""
    return Forme(
        t -> A[1,1]*get_x(forme,t) + A[1,2]*get_y(forme,t),
        t -> A[2,1]*get_x(forme,t) + A[2,2]*get_y(forme,t),
        "transformer($forme.nom, $A))")
end

function decaler(forme::Forme, dx::Float64, dy::Float64)
    """ Renvoie une nouvelle forme, décallée de dx et dy. """
    return Forme(
        t -> get_x(forme,t+dx),
        t -> get_y(forme,t+dy),
        "decaler($forme.nom, $dx, $dy)")
end