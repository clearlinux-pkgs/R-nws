#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-nws
Version  : 1.7.0.1
Release  : 14
URL      : https://cran.r-project.org/src/contrib/nws_1.7.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/nws_1.7.0.1.tar.gz
Summary  : R functions for NetWorkSpaces and Sleigh
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
NetWorkSpaces for R
---------------------
NetWorkSpaces (NWS) is a powerful, easy-to-use software package that
makes it easy to write parallel R programs.  It allows you to easily
launch a set of worker processes on a specified list of machines, and
then submit tasks to those workers.  For many programs, that is all you
need, but for more sophisticated programs, you can take advantage of the
powerful communication layer to directly communicate and coordinate
between the master and worker processes.

%prep
%setup -q -c -n nws

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571869672

%install
export SOURCE_DATE_EPOCH=1571869672
rm -rf %{buildroot}
export LANG=C.UTF-8
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nws
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nws
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library nws
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc nws || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/nws/ChangeLog
/usr/lib64/R/library/nws/DESCRIPTION
/usr/lib64/R/library/nws/INDEX
/usr/lib64/R/library/nws/Meta/Rd.rds
/usr/lib64/R/library/nws/Meta/data.rds
/usr/lib64/R/library/nws/Meta/demo.rds
/usr/lib64/R/library/nws/Meta/features.rds
/usr/lib64/R/library/nws/Meta/hsearch.rds
/usr/lib64/R/library/nws/Meta/links.rds
/usr/lib64/R/library/nws/Meta/nsInfo.rds
/usr/lib64/R/library/nws/Meta/package.rds
/usr/lib64/R/library/nws/NAMESPACE
/usr/lib64/R/library/nws/R/nws
/usr/lib64/R/library/nws/R/nws.rdb
/usr/lib64/R/library/nws/R/nws.rdx
/usr/lib64/R/library/nws/README
/usr/lib64/R/library/nws/README.sleigh
/usr/lib64/R/library/nws/bin/BackgroundLaunch.py
/usr/lib64/R/library/nws/bin/RBabelfishService.py
/usr/lib64/R/library/nws/bin/RNWSSleighWorker.py
/usr/lib64/R/library/nws/bin/RNWSSleighWorker.sh
/usr/lib64/R/library/nws/bin/RSleighService.py
/usr/lib64/R/library/nws/bin/SleighWorkerWrapper.sh
/usr/lib64/R/library/nws/bin/babelfish.R
/usr/lib64/R/library/nws/bin/nwsclient.py
/usr/lib64/R/library/nws/bin/nwsutil.py
/usr/lib64/R/library/nws/bin/sleighmon.R
/usr/lib64/R/library/nws/data/germandata.txt
/usr/lib64/R/library/nws/demo/mandelbrot.R
/usr/lib64/R/library/nws/demo/nwsExample.R
/usr/lib64/R/library/nws/demo/pportfolio.R
/usr/lib64/R/library/nws/demo/sleighExample.R
/usr/lib64/R/library/nws/examples/README
/usr/lib64/R/library/nws/examples/hello.R
/usr/lib64/R/library/nws/examples/ping.R
/usr/lib64/R/library/nws/examples/pong.R
/usr/lib64/R/library/nws/examples/sleigh/birthday.R
/usr/lib64/R/library/nws/examples/sleigh/bootstrap.R
/usr/lib64/R/library/nws/examples/sleigh/cross.R
/usr/lib64/R/library/nws/examples/sleigh/eachWorker_ex.R
/usr/lib64/R/library/nws/examples/sleigh/kmeans.R
/usr/lib64/R/library/nws/examples/sleigh/mandelbrot.R
/usr/lib64/R/library/nws/examples/sleigh/mandelbrot2.R
/usr/lib64/R/library/nws/examples/sleigh/mandelbrot3.R
/usr/lib64/R/library/nws/examples/sleigh/mandelbrot4.R
/usr/lib64/R/library/nws/examples/sleigh/matrix_multiplication.R
/usr/lib64/R/library/nws/examples/sleigh/mc_sim.R
/usr/lib64/R/library/nws/examples/sleigh/nnet-germandata.R
/usr/lib64/R/library/nws/examples/sleigh/nnet.R
/usr/lib64/R/library/nws/examples/sleigh/nonblocking.R
/usr/lib64/R/library/nws/examples/sleigh/nuclearBootstrapInit.R
/usr/lib64/R/library/nws/examples/sleigh/numactl.R
/usr/lib64/R/library/nws/examples/sleigh/par_contestant.R
/usr/lib64/R/library/nws/examples/sleigh/portfolio.R
/usr/lib64/R/library/nws/examples/sleigh/portfolio_race.py
/usr/lib64/R/library/nws/examples/sleigh/pping.R
/usr/lib64/R/library/nws/examples/sleigh/pportfolio.R
/usr/lib64/R/library/nws/examples/sleigh/prandomforest.R
/usr/lib64/R/library/nws/examples/sleigh/prandomforest2.R
/usr/lib64/R/library/nws/examples/sleigh/ring.R
/usr/lib64/R/library/nws/examples/sleigh/rlecuyer.R
/usr/lib64/R/library/nws/examples/sleigh/seq_contestant.R
/usr/lib64/R/library/nws/examples/sleigh/sequentialBootstrap.R
/usr/lib64/R/library/nws/examples/sleigh/sinc.R
/usr/lib64/R/library/nws/examples/sleigh/sinc2.R
/usr/lib64/R/library/nws/examples/sleigh/sinc3.R
/usr/lib64/R/library/nws/examples/sleigh/sleighBootstrap.R
/usr/lib64/R/library/nws/examples/sleigh/sleighBootstrap2.R
/usr/lib64/R/library/nws/examples/sleigh/sleighBootstrap3.R
/usr/lib64/R/library/nws/examples/sleigh/sleighBootstrap4.R
/usr/lib64/R/library/nws/examples/sleigh/sleighHello.R
/usr/lib64/R/library/nws/examples/sleigh/sportfolio.R
/usr/lib64/R/library/nws/help/AnIndex
/usr/lib64/R/library/nws/help/aliases.rds
/usr/lib64/R/library/nws/help/nws.rdb
/usr/lib64/R/library/nws/help/nws.rdx
/usr/lib64/R/library/nws/help/paths.rds
/usr/lib64/R/library/nws/html/00Index.html
/usr/lib64/R/library/nws/html/R.css
