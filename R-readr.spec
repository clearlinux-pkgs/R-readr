#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readr
Version  : 1.3.1
Release  : 15
URL      : https://cran.r-project.org/src/contrib/readr_1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readr_1.3.1.tar.gz
Summary  : Read Rectangular Text Data
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-readr-lib = %{version}-%{release}
Requires: R-BH
Requires: R-Rcpp
Requires: R-clipr
Requires: R-hms
Requires: R-tibble
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-clipr
BuildRequires : R-hms
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
rectangular data (like 'csv', 'tsv', and 'fwf'). It is designed to flexibly
    parse many types of data found in the wild, while still cleanly failing when
    data unexpectedly changes.

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
export SOURCE_DATE_EPOCH=1545405107

%install
export SOURCE_DATE_EPOCH=1545405107
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
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library readr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/readr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/readr/libs/librcon.so.avx2
/usr/lib64/R/library/readr/libs/librcon.so.avx512
/usr/lib64/R/library/readr/libs/readr.so
/usr/lib64/R/library/readr/libs/readr.so.avx2
/usr/lib64/R/library/readr/libs/readr.so.avx512
/usr/lib64/R/library/readr/rcon/librcon.so
