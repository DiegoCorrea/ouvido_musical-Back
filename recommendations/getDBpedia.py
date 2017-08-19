#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON

def getFromDBpedia(search):
    search = search.replace(' ', '_')
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
            ?description
            ?abstract
            (GROUP_CONCAT(DISTINCT ?artist_label;separator=", ") as ?albuns)
            (GROUP_CONCAT(DISTINCT ?genre_label;separator=", ") as ?genres)
            (GROUP_CONCAT(DISTINCT ?hometown_label;separator=", ") as ?home)

        WHERE {
            OPTIONAL {
                dbr:""" + search + """ rdfs:label ?name .
                FILTER (LANG(?name) = 'en').
            }
            OPTIONAL {
                dbr:""" + search + """ dct:description ?description .
                FILTER (LANG(?description) = 'en').
            }
            OPTIONAL {
                dbr:""" + search + """ dbo:abstract ?abstract .
                FILTER (LANG(?abstract) = 'en').
            }
            OPTIONAL {
                dbr:""" + search + """ dbo:artist ?artist.
                dbr:?artist ?artist_label.
                FILTER (LANG(?artist_label) = 'en').
            }
            OPTIONAL {
                dbr:""" + search + """ dbo:hometown ?hometown.
                ?hometown rdfs:label ?hometown_label.
                FILTER (LANG(?hometown_label) = 'en').
            }
            OPTIONAL {
                dbr:""" + search + """ dbo:genre ?genre .
                ?genre rdfs:label ?genre_label.
                FILTER (LANG(?genre_label) = 'en').
            }
        } GROUP BY ?genre_label ?hometown_label ?description ?name ?abstract ?artist_label
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()


    print("======================", results)
    if len(results['results']['bindings']) == 0:
        return None

    band = {}
    band.setdefault("genres", [])
    band.setdefault("home", [])
    band.setdefault("albuns", [])
    band.setdefault("description", {})

    for result in results["results"]["bindings"]:
        for item in results['head']['vars']:
            if item in result:
                if "name" == item:
                    band.setdefault("name", result["name"]["value"])
                if "description" == item:
                    band.setdefault("description", result["description"]["value"])
                if "abstract" == item:
                    band.setdefault("abstract", result["abstract"]["value"])
                if item == "home" and result[item]["value"] not in band[item]:
                    band[item].append(result[item]["value"])
                if item == "genres" and result[item]["value"] not in band[item]:
                    band[item].append(result[item]["value"])
                if item == "albuns" and result[item]["value"] not in band[item]:
                    band[item].append(result[item]["value"])
    '''
    for result in results["results"]["bindings"]:
        band.setdefault("name", result["name"]["value"])

        if "description" in result:
            band.setdefault("description", result["description"]["value"])

        if "abstract" in result:
            band.setdefault("abstract", result["abstract"]["value"])

        if "genres" in result and result["genres"]["value"] not in band["genres"]:
            band["genres"].append(result["genres"]["value"])

        if result["home"]["value"] not in band["home"]:
            band["home"].append(result["home"]["value"])

        if result["albuns"]["value"] not in band["albuns"]:
            band["albuns"].append(result["albuns"]["value"])

    '''

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
    print("\n")
    print("Albuns:",band["albuns"])


    return band
