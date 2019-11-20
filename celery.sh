#!/usr/bin/env bash
celery -A project worker --concurrency=10