"""Routes for API v1.""" ""

import os

from fastapi import APIRouter

from .scrapers import scrapers


router = APIRouter()


router.include_router( router=scrapers.router, prefix="/scraper", tags=["scraper"])
