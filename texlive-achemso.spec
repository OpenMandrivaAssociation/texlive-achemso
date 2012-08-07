# revision 27172
# category Package
# catalog-ctan /macros/latex/contrib/achemso
# catalog-date 2012-07-26 00:18:42 +0200
# catalog-license lppl1.3
# catalog-version 3.7b
Name:		texlive-achemso
Version:	3.7b
Release:	1
Summary:	Support for American Chemical Society journal submissions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/achemso
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides the official macros (achemso.cls) and
BibTeX styles (achemso.bst and biochem.bst) for submission to
the journals of the American Chemical Society. The natmove
package, which moves citations relative to punctuation, is
distributed as part of the bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/achemso/achemso.bst
%{_texmfdistdir}/bibtex/bst/achemso/biochem.bst
%{_texmfdistdir}/tex/latex/achemso/achemso.cls
%{_texmfdistdir}/tex/latex/achemso/achemso.sty
%{_texmfdistdir}/tex/latex/achemso/config/acbcct.cfg
%{_texmfdistdir}/tex/latex/achemso/config/accacs.cfg
%{_texmfdistdir}/tex/latex/achemso/config/achre4.cfg
%{_texmfdistdir}/tex/latex/achemso/config/acncdm.cfg
%{_texmfdistdir}/tex/latex/achemso/config/acsccc.cfg
%{_texmfdistdir}/tex/latex/achemso/config/amclct.cfg
%{_texmfdistdir}/tex/latex/achemso/config/ancac3.cfg
%{_texmfdistdir}/tex/latex/achemso/config/ancham.cfg
%{_texmfdistdir}/tex/latex/achemso/config/bcches.cfg
%{_texmfdistdir}/tex/latex/achemso/config/bichaw.cfg
%{_texmfdistdir}/tex/latex/achemso/config/bipret.cfg
%{_texmfdistdir}/tex/latex/achemso/config/bomaf6.cfg
%{_texmfdistdir}/tex/latex/achemso/config/cgdefu.cfg
%{_texmfdistdir}/tex/latex/achemso/config/chreay.cfg
%{_texmfdistdir}/tex/latex/achemso/config/cmatex.cfg
%{_texmfdistdir}/tex/latex/achemso/config/crtoec.cfg
%{_texmfdistdir}/tex/latex/achemso/config/enfuem.cfg
%{_texmfdistdir}/tex/latex/achemso/config/esthag.cfg
%{_texmfdistdir}/tex/latex/achemso/config/iecred.cfg
%{_texmfdistdir}/tex/latex/achemso/config/inoraj.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jacsat.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jafcau.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jceaax.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jceda8.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jcisd8.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jctcce.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jmcmar.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jnprdf.cfg
%{_texmfdistdir}/tex/latex/achemso/config/joceah.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jpcafh.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jpcbfk.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jpccck.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jpclcd.cfg
%{_texmfdistdir}/tex/latex/achemso/config/jprobs.cfg
%{_texmfdistdir}/tex/latex/achemso/config/langd5.cfg
%{_texmfdistdir}/tex/latex/achemso/config/mamobx.cfg
%{_texmfdistdir}/tex/latex/achemso/config/mpohbp.cfg
%{_texmfdistdir}/tex/latex/achemso/config/nalefd.cfg
%{_texmfdistdir}/tex/latex/achemso/config/oprdfk.cfg
%{_texmfdistdir}/tex/latex/achemso/config/orgnd7.cfg
%{_texmfdistdir}/tex/latex/achemso/config/orlef7.cfg
%{_texmfdistdir}/tex/latex/achemso/natmove.sty
%doc %{_texmfdistdir}/doc/latex/achemso/README
%doc %{_texmfdistdir}/doc/latex/achemso/achemso-demo.bib
%doc %{_texmfdistdir}/doc/latex/achemso/achemso-demo.pdf
%doc %{_texmfdistdir}/doc/latex/achemso/achemso-demo.tex
%doc %{_texmfdistdir}/doc/latex/achemso/achemso.pdf
#- source
%doc %{_texmfdistdir}/source/latex/achemso/achemso.dtx
%doc %{_texmfdistdir}/source/latex/achemso/achemso.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
