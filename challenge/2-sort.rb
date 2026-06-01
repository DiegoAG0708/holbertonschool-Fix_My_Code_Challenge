#!/usr/bin/ruby
# Sort arguments numerically, ignoring non-integers

args = ARGV.select { |a| a.match?(/^[-]?\d+$/) }  # keep only valid integers
args.map!(&:to_i)
args.sort.each do |n|
  puts n
end
