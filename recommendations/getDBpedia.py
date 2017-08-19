#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON

def getFromDBpedia(search = "Caetano_Veloso"):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        prefix dbr: <http://dbpedia.org/resource/>
        prefix dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX mo: <http://purl.org/ontology/mo/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dct: <http://purl.org/dc/terms/>

        SELECT DISTINCT
            ?name
            ?abstract
            ?description
            (GROUP_CONCAT(DISTINCT ?genre_label;separator=", ") as ?genres)
            (GROUP_CONCAT(DISTINCT ?hometown_label;separator=", ") as ?home)

        WHERE {
            dbr:""" + search + """ rdfs:label ?name .
            dbr:""" + search + """ dbo:abstract ?abstract .
            dbr:""" + search + """ dct:description ?description .

            dbr:""" + search + """ dbo:genre ?genre .
            ?genre rdfs:label ?genre_label.

            dbr:""" + search + """ dbo:hometown ?hometown.
            ?hometown rdfs:label ?hometown_label.

            FILTER (LANG(?abstract) = 'en').
            FILTER (LANG(?description) = 'en').
            FILTER (LANG(?genre_label) = 'en').
            FILTER (LANG(?name) = 'en').
            FILTER (LANG(?hometown_label) = 'en').

            OPTIONAL {
                dbr:""" + search + """ dbo:artist ?artist.
                dbr:?artist ?artist_label.
            }
        } GROUP BY ?genre_label ?hometown_label ?description ?name ?abstract
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    band = {}
    band.setdefault("genres", [])
    band.setdefault("home", [])

    for result in results["results"]["bindings"]:
        band.setdefault("name", result["name"]["value"])
        band.setdefault("description", result["description"]["value"])
        band.setdefault("abstract", result["abstract"]["value"])
        if result["genres"]["value"] not in band["genres"]:
            band["genres"].append(result["genres"]["value"])
        if result["home"]["value"] not in band["home"]:
            band["home"].append(result["home"]["value"])


    print("=======================================================")
    print("\n")
    print("Nome:",band["name"])
    print("\n")
    print("Descrição:",band["description"])
    print("\n")
    print("Resumo:",band["abstract"])
    print("\n")
    print("Generos:",band["genres"])
    print("\n")
    print("Moradia:",band["home"])

    return band
