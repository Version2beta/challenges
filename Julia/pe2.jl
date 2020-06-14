function fibs_less_than(n::Int64, fib::Array{Int64,1})
    next = sum(fib[end - 1:end])::Int64
    next < n && return fibs_less_than(n, push!(fib, next))
    fib
end

function sum_even_reduce(fibs::Array{Int64,1})
    reduce((x, y)->iseven(y) ? x + y : x, fibs)
end

@time result = fibs_less_than(4_000_000, [0, 1]) |> sum_even_reduce
println(result)