#!/usr/bin/ruby
# Sort arguments numerically

args = ARGV.map(&:to_i)   # convert all arguments to integers
args.sort.each do |n|
  puts n
end
