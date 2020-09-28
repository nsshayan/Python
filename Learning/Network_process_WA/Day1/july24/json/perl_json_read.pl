#!/usr/bin/env perl 
use strict;
use warnings;
use JSON qw(decode_json);
use Data::Dumper;

open FH, "data.json" or die "$0: data.json: $!\n";
my $contents = <FH>;
close FH;

my $data = decode_json($contents);

print Dumper($data);



