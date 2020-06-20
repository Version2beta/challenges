# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

using DelimitedFiles
primes = DelimitedFiles.readdlm("../first_million_primes.txt", ',', BigInt) |> vec

function factors(n, d=2, f=BigInt[])
    n < 2 && return f
    while d^2 < n
        if n % d == 0
            n = div(n, d)
            f = push!(f, d)
        else
            d += 1
        end
    end
    push!(f, n)
end

function test()
    samples = rand(primes, 8) |> sort!
    n = reduce(*, samples)
    f = factors(n)
end