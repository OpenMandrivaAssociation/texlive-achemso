%global tl_name achemso
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.14
Release:	%{tl_revision}.1
Summary:	Support for American Chemical Society journal submissions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/achemso
License:	lppl1.3c other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/achemso.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a BibTeX style file following the requirements of
the American Chemical Society (ACS), and a package to pass settings to
the BibTeX style. It also includes a class which was used for submission
support in the past. All of this material is largely of historical
interest and is retained for stability. For new material, the chem-acs
style is available for bibliographies, and a short template for the ACS
website is better suited to submission.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/achemso
%dir %{_datadir}/texmf-dist/doc/latex/achemso
%dir %{_datadir}/texmf-dist/source/latex/achemso
%dir %{_datadir}/texmf-dist/tex/latex/achemso
%{_datadir}/texmf-dist/bibtex/bst/achemso/achemso.bst
%{_datadir}/texmf-dist/bibtex/bst/achemso/biochem.bst
%doc %{_datadir}/texmf-dist/doc/latex/achemso/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/achemso/LICENSE.md
%doc %{_datadir}/texmf-dist/doc/latex/achemso/README.md
%doc %{_datadir}/texmf-dist/doc/latex/achemso/achemso-demo.bib
%doc %{_datadir}/texmf-dist/doc/latex/achemso/achemso-demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/achemso/achemso-demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/achemso/achemso.pdf
%doc %{_datadir}/texmf-dist/source/latex/achemso/achemso.dtx
%doc %{_datadir}/texmf-dist/source/latex/achemso/achemso.ins
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aaembp.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aaemcq.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aamick.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aanmf6.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aapmcd.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aastgj.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-abmcb8.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-abseba.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-acbcct.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-accacs.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-achre4.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-acncdm.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-acsccc.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-acscii.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-acsodf.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aeacb3.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aeacc4.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aeecco.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aelccp.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aesccq.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aewcaa.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-afsthl.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aidcbc.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amacgu.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amachv.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amclct.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amlccd.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amlcef.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-amrcda.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-anaccx.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-ancac3.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-ancham.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-anmafm.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-aoiab5.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-apcach.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-apchd5.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-appccd.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-asbcd6.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-ascecg.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-ascefj.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-bcches.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-bichaw.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-bomaf6.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-cgdefu.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-chreay.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-cmatex.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-crtoec.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-enfuem.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-esthag.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-estlcu.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-iecred.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-inoraj.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jaaucr.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jacsat.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jafcau.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jceaax.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jceda8.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jcisd8.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jctcce.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jmcmar.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jnprdf.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-joceah.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jpcafh.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jpcbfk.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jpccck.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jpclcd.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-jprobs.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-langd5.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-mamobx.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-mpohbp.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-nalefd.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-oprdfk.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-orgnd7.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso-orlef7.cfg
%{_datadir}/texmf-dist/tex/latex/achemso/achemso.cls
%{_datadir}/texmf-dist/tex/latex/achemso/achemso.sty
%{_datadir}/texmf-dist/tex/latex/achemso/natmove.sty
