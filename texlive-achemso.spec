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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a BibTeX style file following the requirements of
the American Chemical Society (ACS), and a package to pass settings to
the BibTeX style. It also includes a class which was used for submission
support in the past. All of this material is largely of historical
interest and is retained for stability. For new material, the chem-acs
style is available for bibliographies, and a short template for the ACS
website is better suited to submission.

