Name:		texlive-achemso
Version:	69638
Release:	1
Summary:	Support for American Chemical Society journal submissions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/achemso
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/achemso
%{_texmfdistdir}/tex/latex/achemso
%doc %{_texmfdistdir}/doc/latex/achemso
#- source
%doc %{_texmfdistdir}/source/latex/achemso

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
