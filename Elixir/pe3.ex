# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

{:ok, primes_string} = File.read("../first_million_primes.txt")

defmodule PrimeFactors do
  def factors(n, d \\ 2, f \\ [])
  def factors(n, _d, _f) when n < 2, do: []
  def factors(n, d, f) when d * d > n, do: [n | f]
  def factors(n, d, f) when rem(n, d) == 0, do: factors(div(n, d), d, [d | f])
  def factors(n, d, f), do: factors(n, d + 1, f)

  def largest(n), do: factors(n) |> List.first()

  @primes primes_string
          |> String.split(",")
          |> Enum.map(fn s -> String.trim(s) |> String.to_integer() end)

  def test() do
    ((factors(13195) == [29, 13, 7, 5] && :passed) || :failed) |> IO.inspect(label: :pe_example)

    primes =
      @primes
      |> Enum.take_random(16)
      |> Enum.sort(:desc)

    n = Enum.reduce(primes, &Kernel.*/2)

    {time, result} = :timer.tc(PrimeFactors.IntegerDivision, :factors, [n])
    ((result == primes && :passed) || :failed) |> IO.inspect(label: :big_example)
    IO.puts("#{time / 1000} miliseconds to compute factors of #{n}: #{inspect(result)}")

    (result == primes && :passed) ||
      :failed |> IO.inspect(label: :big_example)

    largest(600_851_475_143) |> IO.inspect(label: :largest_prime_of_600_851_475_143)
    :done
  end
end
