#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readr
Version  : 1.3.1
Release  : 18
URL      : https://cran.r-project.org/src/contrib/readr_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readr_1.3.1.tar.gz
Summary  : Improved methods for reading rectangular data.
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-readr-lib = %{version}-%{release}
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-clipr
BuildRequires : R-hms
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
# readr <a href="https://readr.tidyverse.org"><img src="man/figures/logo.png" align="right" height = 150 /></a>

%package lib
Summary: lib components for the R-readr package.
Group: Libraries

%description lib
lib components for the R-readr package.


%prep
%setup -q -c -n readr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552836236

%install
export SOURCE_DATE_EPOCH=1552836236
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  readr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/readr/DESCRIPTION
/usr/lib64/R/library/readr/INDEX
/usr/lib64/R/library/readr/LICENSE
/usr/lib64/R/library/readr/Meta/Rd.rds
/usr/lib64/R/library/readr/Meta/features.rds
/usr/lib64/R/library/readr/Meta/hsearch.rds
/usr/lib64/R/library/readr/Meta/links.rds
/usr/lib64/R/library/readr/Meta/nsInfo.rds
/usr/lib64/R/library/readr/Meta/package.rds
/usr/lib64/R/library/readr/Meta/vignette.rds
/usr/lib64/R/library/readr/NAMESPACE
/usr/lib64/R/library/readr/NEWS.md
/usr/lib64/R/library/readr/R/readr
/usr/lib64/R/library/readr/R/readr.rdb
/usr/lib64/R/library/readr/R/readr.rdx
/usr/lib64/R/library/readr/R/sysdata.rdb
/usr/lib64/R/library/readr/R/sysdata.rdx
/usr/lib64/R/library/readr/WORDLIST
/usr/lib64/R/library/readr/doc/index.html
/usr/lib64/R/library/readr/doc/locales.R
/usr/lib64/R/library/readr/doc/locales.Rmd
/usr/lib64/R/library/readr/doc/locales.html
/usr/lib64/R/library/readr/doc/readr.R
/usr/lib64/R/library/readr/doc/readr.Rmd
/usr/lib64/R/library/readr/doc/readr.html
/usr/lib64/R/library/readr/extdata/challenge.csv
/usr/lib64/R/library/readr/extdata/epa78.txt
/usr/lib64/R/library/readr/extdata/example.log
/usr/lib64/R/library/readr/extdata/fwf-sample.txt
/usr/lib64/R/library/readr/extdata/massey-rating.txt
/usr/lib64/R/library/readr/extdata/mtcars.csv
/usr/lib64/R/library/readr/extdata/mtcars.csv.bz2
/usr/lib64/R/library/readr/extdata/mtcars.csv.zip
/usr/lib64/R/library/readr/help/AnIndex
/usr/lib64/R/library/readr/help/aliases.rds
/usr/lib64/R/library/readr/help/figures/logo.png
/usr/lib64/R/library/readr/help/paths.rds
/usr/lib64/R/library/readr/help/readr.rdb
/usr/lib64/R/library/readr/help/readr.rdx
/usr/lib64/R/library/readr/html/00Index.html
/usr/lib64/R/library/readr/html/R.css
/usr/lib64/R/library/readr/tests/spelling.R
/usr/lib64/R/library/readr/tests/testthat.R
/usr/lib64/R/library/readr/tests/testthat/basic-df-singlequote.csv
/usr/lib64/R/library/readr/tests/testthat/basic-df.csv
/usr/lib64/R/library/readr/tests/testthat/colour-test
/usr/lib64/R/library/readr/tests/testthat/empty-file
/usr/lib64/R/library/readr/tests/testthat/enc-iso-8859-1.txt
/usr/lib64/R/library/readr/tests/testthat/eol-cr.csv
/usr/lib64/R/library/readr/tests/testthat/eol-cr.txt
/usr/lib64/R/library/readr/tests/testthat/eol-cr.txt.bz2
/usr/lib64/R/library/readr/tests/testthat/eol-cr.txt.gz
/usr/lib64/R/library/readr/tests/testthat/eol-cr.txt.xz
/usr/lib64/R/library/readr/tests/testthat/eol-cr.txt.zip
/usr/lib64/R/library/readr/tests/testthat/eol-crlf.csv
/usr/lib64/R/library/readr/tests/testthat/eol-crlf.txt
/usr/lib64/R/library/readr/tests/testthat/eol-lf.csv
/usr/lib64/R/library/readr/tests/testthat/eol-lf.txt
/usr/lib64/R/library/readr/tests/testthat/fwf-trailing.txt
/usr/lib64/R/library/readr/tests/testthat/helper.R
/usr/lib64/R/library/readr/tests/testthat/non-tabular.csv
/usr/lib64/R/library/readr/tests/testthat/null-file
/usr/lib64/R/library/readr/tests/testthat/raw.csv
/usr/lib64/R/library/readr/tests/testthat/sample_text.txt
/usr/lib64/R/library/readr/tests/testthat/table-crash
/usr/lib64/R/library/readr/tests/testthat/test-col-spec.R
/usr/lib64/R/library/readr/tests/testthat/test-collectors.R
/usr/lib64/R/library/readr/tests/testthat/test-encoding.R
/usr/lib64/R/library/readr/tests/testthat/test-eol.R
/usr/lib64/R/library/readr/tests/testthat/test-locale.R
/usr/lib64/R/library/readr/tests/testthat/test-melt-chunked.R
/usr/lib64/R/library/readr/tests/testthat/test-melt-csv.R
/usr/lib64/R/library/readr/tests/testthat/test-melt-fwf.R
/usr/lib64/R/library/readr/tests/testthat/test-melt-table.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-character.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-count-fields.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-datetime.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-factors.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-logical.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-numeric.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing-time.R
/usr/lib64/R/library/readr/tests/testthat/test-parsing.R
/usr/lib64/R/library/readr/tests/testthat/test-problems.R
/usr/lib64/R/library/readr/tests/testthat/test-read-chunked.R
/usr/lib64/R/library/readr/tests/testthat/test-read-csv.R
/usr/lib64/R/library/readr/tests/testthat/test-read-file.R
/usr/lib64/R/library/readr/tests/testthat/test-read-fwf.R
/usr/lib64/R/library/readr/tests/testthat/test-read-lines.R
/usr/lib64/R/library/readr/tests/testthat/test-read-table.R
/usr/lib64/R/library/readr/tests/testthat/test-source.R
/usr/lib64/R/library/readr/tests/testthat/test-tokenizer-delim.R
/usr/lib64/R/library/readr/tests/testthat/test-type-convert.R
/usr/lib64/R/library/readr/tests/testthat/test-write-lines.R
/usr/lib64/R/library/readr/tests/testthat/test-write.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/readr/libs/readr.so
/usr/lib64/R/library/readr/libs/readr.so.avx2
/usr/lib64/R/library/readr/libs/readr.so.avx512
/usr/lib64/R/library/readr/rcon/librcon.so
